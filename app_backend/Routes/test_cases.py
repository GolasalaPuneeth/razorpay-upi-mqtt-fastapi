from fastapi import APIRouter
from App_Utils import MQTTTool

testcases = APIRouter(tags=["Test Cases Execution Point"], prefix="/tests")
mqtttool:MQTTTool = MQTTTool()


@testcases.get("/")
async def test_Mqtt():
    mqtttool.publish_message("test","hello")
    print("Executed in route")
    return []