from fastapi import APIRouter, Depends
from App_Utils import MQTTTool
from Celery_worker import test_task

testcases = APIRouter(tags=["Test Cases Execution Point"], prefix="/tests")
mqtttool:MQTTTool = MQTTTool()


@testcases.get("/")
async def test_Mqtt():
    # mqtttool.publish_message("test","hello")
    # print("Executed in route")
    test_task.delay("sample_data")
    return []