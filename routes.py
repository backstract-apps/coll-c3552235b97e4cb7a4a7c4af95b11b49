from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/opportunities/')
async def post_opportunities(raw_data: schemas.PostOpportunities, db: Session = Depends(get_db)):
    try:
        return await service.post_opportunities(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/opportunities/id/')
async def put_opportunities_id(id: int, customer_id: int, potential_value: Annotated[str, Query(max_length=100)], stage: Annotated[str, Query(max_length=100)], expected_close_date: str, db: Session = Depends(get_db)):
    try:
        return await service.put_opportunities_id(db, id, customer_id, potential_value, stage, expected_close_date)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/opportunities/id')
async def delete_opportunities_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_opportunities_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/id/')
async def put_customers_id(id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_customers_id(db, id, name, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/customers/id')
async def delete_customers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/interactions/')
async def get_interactions(db: Session = Depends(get_db)):
    try:
        return await service.get_interactions(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/interactions/')
async def post_interactions(raw_data: schemas.PostInteractions, db: Session = Depends(get_db)):
    try:
        return await service.post_interactions(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/interactions/id')
async def delete_interactions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_interactions_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/opportunities/id')
async def get_opportunities_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_opportunities_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/')
async def get_customers(headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/interactions/id')
async def get_interactions_id(id: str, test_params: str, arun: str, db: Session = Depends(get_db)):
    try:
        return await service.get_interactions_id(db, id, test_params, arun)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/opportunities/')
async def get_opportunities(db: Session = Depends(get_db)):
    try:
        return await service.get_opportunities(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(raw_data: schemas.PostCustomers, db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/id')
async def get_customers_id(id: str, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/interactions/id/')
async def put_interactions_id(id: int, customer_id: int, date: str, time: Annotated[str, Query(max_length=100)], summary: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_interactions_id(db, id, customer_id, date, time, summary)
    except Exception as e:
        raise HTTPException(500, str(e))

