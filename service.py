from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def post_opportunities(db: Session, raw_data: schemas.PostOpportunities):
    id: int = raw_data.id
    customer_id: int = raw_data.customer_id
    potential_value: str = raw_data.potential_value
    stage: str = raw_data.stage
    expected_close_date: datetime.date = raw_data.expected_close_date

    record_to_be_added = {
        "id": id,
        "stage": stage,
        "customer_id": customer_id,
        "potential_value": potential_value,
        "expected_close_date": expected_close_date,
    }
    new_opportunities = models.Opportunities(**record_to_be_added)
    db.add(new_opportunities)
    db.commit()
    db.refresh(new_opportunities)
    opportunities_inserted_record = new_opportunities.to_dict()

    res = {
        "opportunities_inserted_record": opportunities_inserted_record,
    }
    return res


async def put_opportunities_id(
    db: Session,
    id: int,
    customer_id: int,
    potential_value: str,
    stage: str,
    expected_close_date: str,
):

    query = db.query(models.Opportunities)
    query = query.filter(and_(models.Opportunities.id == id))
    opportunities_edited_record = query.first()

    if opportunities_edited_record:
        for key, value in {
            "id": id,
            "stage": stage,
            "customer_id": customer_id,
            "potential_value": potential_value,
            "expected_close_date": expected_close_date,
        }.items():
            setattr(opportunities_edited_record, key, value)

        db.commit()
        db.refresh(opportunities_edited_record)

        opportunities_edited_record = (
            opportunities_edited_record.to_dict()
            if hasattr(opportunities_edited_record, "to_dict")
            else vars(opportunities_edited_record)
        )
    res = {
        "opportunities_edited_record": opportunities_edited_record,
    }
    return res


async def delete_opportunities_id(db: Session, id: int):

    query = db.query(models.Opportunities)
    query = query.filter(and_(models.Opportunities.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        opportunities_deleted = record_to_delete.to_dict()
    else:
        opportunities_deleted = record_to_delete
    res = {
        "opportunities_deleted": opportunities_deleted,
    }
    return res


async def put_customers_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )
    res = {
        "customers_edited_record": customers_edited_record,
    }
    return res


async def delete_customers_id(db: Session, id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete
    res = {
        "customers_deleted": customers_deleted,
    }
    return res


async def get_interactions(db: Session):

    query = db.query(models.Interactions)

    interactions_all = query.all()
    interactions_all = (
        [new_data.to_dict() for new_data in interactions_all]
        if interactions_all
        else interactions_all
    )
    res = {
        "interactions_all": interactions_all,
    }
    return res


async def post_interactions(db: Session, raw_data: schemas.PostInteractions):
    id: int = raw_data.id
    customer_id: int = raw_data.customer_id
    date: datetime.date = raw_data.date
    time: str = raw_data.time
    summary: str = raw_data.summary

    record_to_be_added = {
        "id": id,
        "date": date,
        "time": time,
        "summary": summary,
        "customer_id": customer_id,
    }
    new_interactions = models.Interactions(**record_to_be_added)
    db.add(new_interactions)
    db.commit()
    db.refresh(new_interactions)
    interactions_inserted_record = new_interactions.to_dict()

    res = {
        "interactions_inserted_record": interactions_inserted_record,
    }
    return res


async def delete_interactions_id(db: Session, id: int):

    query = db.query(models.Interactions)
    query = query.filter(and_(models.Interactions.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        interactions_deleted = record_to_delete.to_dict()
    else:
        interactions_deleted = record_to_delete
    res = {
        "interactions_deleted": interactions_deleted,
    }
    return res


async def get_opportunities_id(db: Session, id: int):

    query = db.query(models.Opportunities)
    query = query.filter(and_(models.Opportunities.id == id))

    opportunities_one = query.first()

    opportunities_one = (
        (
            opportunities_one.to_dict()
            if hasattr(opportunities_one, "to_dict")
            else vars(opportunities_one)
        )
        if opportunities_one
        else opportunities_one
    )

    res = {
        "opportunities_one": opportunities_one,
    }
    return res


async def get_customers(db: Session, request: Request):
    header_dasd: Any = request.headers.get("header-dasd")

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )
    res = {
        "customers_all": customers_all,
    }
    return res


async def get_interactions_id(db: Session, id: str, test_params: str, arun: str):

    query = db.query(models.Interactions)
    query = query.filter(and_(models.Interactions.id == id))

    interactions_one = query.first()

    interactions_one = (
        (
            interactions_one.to_dict()
            if hasattr(interactions_one, "to_dict")
            else vars(interactions_one)
        )
        if interactions_one
        else interactions_one
    )

    headers = {}
    auth = ("", "")
    payload = {}
    apiResponse = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    sample_posts = (
        apiResponse.json() if "list" in ["dict", "list"] else apiResponse.text
    )
    res = {
        "interactions_one": interactions_one,
    }
    return res


async def get_opportunities(db: Session):

    query = db.query(models.Opportunities)

    opportunities_all = query.all()
    opportunities_all = (
        [new_data.to_dict() for new_data in opportunities_all]
        if opportunities_all
        else opportunities_all
    )

    headers = {}
    auth = ("", "")
    payload = {}
    apiResponse = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    sample_posts = (
        apiResponse.json() if "list" in ["dict", "list"] else apiResponse.text
    )
    res = {
        "opportunities_all": opportunities_all,
    }
    return res


async def post_customers(db: Session, raw_data: schemas.PostCustomers):
    id: int = raw_data.id
    name: int = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"id": id, "name": name, "contact_details": contact_details}
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "customers_inserted_record": customers_inserted_record,
    }
    return res


async def get_customers_id(db: Session, id: str):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "customers_one": customers_one,
    }
    return res


async def put_interactions_id(
    db: Session, id: int, customer_id: int, date: str, time: str, summary: str
):

    query = db.query(models.Interactions)
    query = query.filter(and_(models.Interactions.id == id))
    interactions_edited_record = query.first()

    if interactions_edited_record:
        for key, value in {
            "id": id,
            "date": date,
            "time": time,
            "summary": summary,
            "customer_id": customer_id,
        }.items():
            setattr(interactions_edited_record, key, value)

        db.commit()
        db.refresh(interactions_edited_record)

        interactions_edited_record = (
            interactions_edited_record.to_dict()
            if hasattr(interactions_edited_record, "to_dict")
            else vars(interactions_edited_record)
        )
    res = {
        "interactions_edited_record": interactions_edited_record,
    }
    return res
