from fastapi import APIRouter, Depends
from sqlmodel import Session
from App_Utils import MQTTTool
from Celery_worker import test_task
from Database_Layer import get_sync_session
testcases = APIRouter(tags=["Test Cases Execution Point"], prefix="/tests")
mqtttool:MQTTTool = MQTTTool()


@testcases.get("/")
async def test_Mqtt(sync_session: Session=Depends(get_sync_session)):
    # mqtttool.publish_message("test","hello")
    # print("Executed in route")
    test_task.delay("sample_data",sync_session)
    return []