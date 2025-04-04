# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taskService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11taskService.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xcf\x01\n\nTaskConfig\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x17\n\x06taskID\x18\x02 \x01(\x0b\x32\x07.TaskID\x12\x17\n\x06target\x18\x03 \x01(\x0b\x32\x07.Target\x12#\n\x0coperatorFlow\x18\x04 \x01(\x0b\x32\r.OperatorFlow\x12-\n\x11logicalSimulation\x18\x05 \x01(\x0b\x32\x12.LogicalSimulation\x12+\n\x10\x64\x65viceSimulation\x18\x06 \x01(\x0b\x32\x11.DeviceSimulation\";\n\x06Target\x12\x1f\n\ntargetData\x18\x01 \x03(\x0b\x32\x0b.TargetData\x12\x10\n\x08priority\x18\x02 \x01(\x05\"\xd2\x01\n\nTargetData\x12\x10\n\x08\x64\x61taName\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61taPath\x18\x02 \x01(\t\x12\x15\n\rdataSplitType\x18\x03 \x01(\x08\x12+\n\x10\x64\x61taTransferType\x18\x04 \x01(\x0e\x32\x11.FileTransferType\x12\x10\n\x08taskType\x18\x05 \x01(\t\x12)\n\x0ftotalSimulation\x18\x06 \x01(\x0b\x32\x10.TotalSimulation\x12\x1f\n\nallocation\x18\x07 \x01(\x0b\x32\x0b.Allocation\"o\n\x0fTotalSimulation\x12\x1d\n\x15\x64\x65viceTotalSimulation\x18\x01 \x03(\t\x12\x1a\n\x12numTotalSimulation\x18\x02 \x03(\x05\x12!\n\x19\x64ynamicNumTotalSimulation\x18\x03 \x03(\x05\"\x96\x01\n\nAllocation\x12\x14\n\x0coptimization\x18\x01 \x01(\x08\x12#\n\x1b\x61llocationLogicalSimulation\x18\x02 \x03(\x05\x12\"\n\x1a\x61llocationDeviceSimulation\x18\x03 \x03(\x05\x12)\n\x0frunningResponse\x18\x04 \x01(\x0b\x32\x10.RunningResponse\"L\n\x0fRunningResponse\x12\x1d\n\x15\x64\x65viceRunningResponse\x18\x01 \x03(\t\x12\x1a\n\x12numRunningResponse\x18\x02 \x03(\x05\"N\n\x0cOperatorFlow\x12!\n\x0b\x66lowSetting\x18\x01 \x01(\x0b\x32\x0c.FlowSetting\x12\x1b\n\x08operator\x18\x02 \x03(\x0b\x32\t.Operator\"{\n\x0b\x46lowSetting\x12\r\n\x05round\x18\x01 \x01(\x05\x12.\n\x0estartCondition\x18\x02 \x01(\x0b\x32\x16.OperatorFlowCondition\x12-\n\rstopCondition\x18\x03 \x01(\x0b\x32\x16.OperatorFlowCondition\"\x84\x01\n\x15OperatorFlowCondition\x12\x35\n\x19logicalSimulationStrategy\x18\x01 \x01(\x0b\x32\x12.StrategyCondition\x12\x34\n\x18\x64\x65viceSimulationStrategy\x18\x02 \x01(\x0b\x32\x12.StrategyCondition\"Z\n\x11StrategyCondition\x12\x19\n\x11strategyCondition\x18\x01 \x01(\t\x12\x14\n\x0cwaitInterval\x18\x02 \x01(\x05\x12\x14\n\x0ctotalTimeout\x18\x03 \x01(\x05\"\x91\x02\n\x08Operator\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x41\n\x1boperationBehaviorController\x18\x02 \x01(\x0b\x32\x1c.OperationBehaviorController\x12\r\n\x05input\x18\x03 \x03(\t\x12\x0f\n\x07useData\x18\x04 \x01(\x08\x12\x15\n\x05model\x18\x05 \x01(\x0b\x32\x06.Model\x12>\n\x1dlogicalSimulationOperatorInfo\x18\x06 \x01(\x0b\x32\x17.OperatorSimulationInfo\x12=\n\x1c\x64\x65viceSimulationOperatorInfo\x18\x07 \x01(\x0b\x32\x17.OperatorSimulationInfo\"q\n\x1bOperationBehaviorController\x12\x15\n\ruseController\x18\x01 \x01(\x08\x12\"\n\x1astrategyBehaviorController\x18\x02 \x01(\t\x12\x17\n\x0foutboundService\x18\x03 \x01(\t\"\x8b\x01\n\x05Model\x12\x10\n\x08useModel\x18\x01 \x01(\x08\x12\x15\n\rmodelForTrain\x18\x02 \x01(\x08\x12,\n\x11modelTransferType\x18\x03 \x01(\x0e\x32\x11.FileTransferType\x12\x11\n\tmodelPath\x18\x04 \x01(\t\x12\x18\n\x10modelUpdateStyle\x18\x05 \x01(\t\"\x96\x01\n\x16OperatorSimulationInfo\x12/\n\x14operatorTransferType\x18\x01 \x01(\x0e\x32\x11.FileTransferType\x12\x18\n\x10operatorCodePath\x18\x02 \x01(\t\x12\x19\n\x11operatorEntryFile\x18\x03 \x01(\t\x12\x16\n\x0eoperatorParams\x18\x04 \x01(\t\"z\n\x11LogicalSimulation\x12)\n\x0f\x63omputationUnit\x18\x01 \x01(\x0b\x32\x10.ComputationUnit\x12:\n resourceRequestLogicalSimulation\x18\x02 \x03(\x0b\x32\x10.ResourceRequest\"I\n\x0f\x43omputationUnit\x12\x13\n\x0b\x64\x65vicesUnit\x18\x01 \x03(\t\x12!\n\x0bunitSetting\x18\x02 \x03(\x0b\x32\x0c.UnitSetting\"\x1e\n\x0bUnitSetting\x12\x0f\n\x07numCpus\x18\x01 \x01(\x05\"m\n\x0fResourceRequest\x12\x1f\n\x17\x64\x61taNameResourceRequest\x18\x01 \x01(\t\x12\x1d\n\x15\x64\x65viceResourceRequest\x18\x02 \x03(\t\x12\x1a\n\x12numResourceRequest\x18\x03 \x03(\x05\"M\n\x10\x44\x65viceSimulation\x12\x39\n\x1fresourceRequestDeviceSimulation\x18\x01 \x03(\x0b\x32\x10.ResourceRequest\"\x18\n\x06TaskID\x12\x0e\n\x06taskID\x18\x01 \x01(\t\"#\n\tTaskQueue\x12\x16\n\x05tasks\x18\x01 \x03(\x0b\x32\x07.TaskID\"1\n\nTaskStatus\x12#\n\ntaskStatus\x18\x01 \x01(\x0e\x32\x0f.TaskStatusEnum\"%\n\x0fOperationStatus\x12\x12\n\nis_success\x18\x01 \x01(\x08\"\x1e\n\tScheduler\x12\x11\n\tscheduler\x18\x01 \x01(\t\"\xcb\x01\n\x10\x44\x65viceTaskConfig\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x0e\n\x06taskID\x18\x02 \x01(\t\x12+\n\x10\x64\x65viceTargetData\x18\x03 \x03(\x0b\x32\x11.DeviceTargetData\x12/\n\x12\x64\x65viceOperatorFlow\x18\x04 \x01(\x0b\x32\x13.DeviceOperatorFlow\x12\x39\n\x1fresourceRequestDeviceSimulation\x18\x05 \x03(\x0b\x32\x10.ResourceRequest\"\xee\x01\n\x10\x44\x65viceTargetData\x12\x10\n\x08\x64\x61taName\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61taPath\x18\x02 \x01(\t\x12\x15\n\rdataSplitType\x18\x03 \x01(\x08\x12+\n\x10\x64\x61taTransferType\x18\x04 \x01(\x0e\x32\x11.FileTransferType\x12\x10\n\x08taskType\x18\x05 \x01(\t\x12\x35\n\x15\x64\x65viceTotalSimulation\x18\x06 \x01(\x0b\x32\x16.DeviceTotalSimulation\x12)\n\x0frunningResponse\x18\x07 \x01(\x0b\x32\x10.RunningResponse\"6\n\x15\x44\x65viceTotalSimulation\x12\x0f\n\x07\x64\x65vices\x18\x01 \x03(\t\x12\x0c\n\x04nums\x18\x02 \x03(\x05\"l\n\x12\x44\x65viceOperatorFlow\x12-\n\x11\x64\x65viceFlowSetting\x18\x01 \x01(\x0b\x32\x12.DeviceFlowSetting\x12\'\n\x0e\x64\x65viceOperator\x18\x02 \x03(\x0b\x32\x0f.DeviceOperator\"\x85\x01\n\x11\x44\x65viceFlowSetting\x12\r\n\x05round\x18\x01 \x01(\x05\x12\x30\n\x14\x64\x65viceStartCondition\x18\x02 \x01(\x0b\x32\x12.StrategyCondition\x12/\n\x13\x64\x65viceStopCondition\x18\x03 \x01(\x0b\x32\x12.StrategyCondition\"\xd7\x01\n\x0e\x44\x65viceOperator\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x41\n\x1boperationBehaviorController\x18\x02 \x01(\x0b\x32\x1c.OperationBehaviorController\x12\r\n\x05input\x18\x03 \x03(\t\x12\x0f\n\x07useData\x18\x04 \x01(\x08\x12\x15\n\x05model\x18\x05 \x01(\x0b\x32\x06.Model\x12=\n\x1c\x64\x65viceSimulationOperatorInfo\x18\x06 \x01(\x0b\x32\x17.OperatorSimulationInfo*9\n\x10\x46ileTransferType\x12\x08\n\x04\x46ILE\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\x06\n\x02S3\x10\x02\x12\t\n\x05MINIO\x10\x03*w\n\x0eTaskStatusEnum\x12\r\n\tSUCCEEDED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0b\n\x07STOPPED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07MISSING\x10\x05\x12\n\n\x06UNDONE\x10\x06\x12\n\n\x06QUEUED\x10\x07\x32\xe9\x01\n\x07TaskMgr\x12+\n\nsubmitTask\x12\x0b.TaskConfig\x1a\x10.OperationStatus\x12%\n\x08stopTask\x12\x07.TaskID\x1a\x10.OperationStatus\x12%\n\rgetTaskStatus\x12\x07.TaskID\x1a\x0b.TaskStatus\x12\x32\n\x0cgetTaskQueue\x12\x16.google.protobuf.Empty\x1a\n.TaskQueue\x12/\n\x0f\x63hangeScheduler\x12\n.Scheduler\x1a\x10.OperationStatusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'taskService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILETRANSFERTYPE._serialized_start=3569
  _FILETRANSFERTYPE._serialized_end=3626
  _TASKSTATUSENUM._serialized_start=3628
  _TASKSTATUSENUM._serialized_end=3747
  _TASKCONFIG._serialized_start=51
  _TASKCONFIG._serialized_end=258
  _TARGET._serialized_start=260
  _TARGET._serialized_end=319
  _TARGETDATA._serialized_start=322
  _TARGETDATA._serialized_end=532
  _TOTALSIMULATION._serialized_start=534
  _TOTALSIMULATION._serialized_end=645
  _ALLOCATION._serialized_start=648
  _ALLOCATION._serialized_end=798
  _RUNNINGRESPONSE._serialized_start=800
  _RUNNINGRESPONSE._serialized_end=876
  _OPERATORFLOW._serialized_start=878
  _OPERATORFLOW._serialized_end=956
  _FLOWSETTING._serialized_start=958
  _FLOWSETTING._serialized_end=1081
  _OPERATORFLOWCONDITION._serialized_start=1084
  _OPERATORFLOWCONDITION._serialized_end=1216
  _STRATEGYCONDITION._serialized_start=1218
  _STRATEGYCONDITION._serialized_end=1308
  _OPERATOR._serialized_start=1311
  _OPERATOR._serialized_end=1584
  _OPERATIONBEHAVIORCONTROLLER._serialized_start=1586
  _OPERATIONBEHAVIORCONTROLLER._serialized_end=1699
  _MODEL._serialized_start=1702
  _MODEL._serialized_end=1841
  _OPERATORSIMULATIONINFO._serialized_start=1844
  _OPERATORSIMULATIONINFO._serialized_end=1994
  _LOGICALSIMULATION._serialized_start=1996
  _LOGICALSIMULATION._serialized_end=2118
  _COMPUTATIONUNIT._serialized_start=2120
  _COMPUTATIONUNIT._serialized_end=2193
  _UNITSETTING._serialized_start=2195
  _UNITSETTING._serialized_end=2225
  _RESOURCEREQUEST._serialized_start=2227
  _RESOURCEREQUEST._serialized_end=2336
  _DEVICESIMULATION._serialized_start=2338
  _DEVICESIMULATION._serialized_end=2415
  _TASKID._serialized_start=2417
  _TASKID._serialized_end=2441
  _TASKQUEUE._serialized_start=2443
  _TASKQUEUE._serialized_end=2478
  _TASKSTATUS._serialized_start=2480
  _TASKSTATUS._serialized_end=2529
  _OPERATIONSTATUS._serialized_start=2531
  _OPERATIONSTATUS._serialized_end=2568
  _SCHEDULER._serialized_start=2570
  _SCHEDULER._serialized_end=2600
  _DEVICETASKCONFIG._serialized_start=2603
  _DEVICETASKCONFIG._serialized_end=2806
  _DEVICETARGETDATA._serialized_start=2809
  _DEVICETARGETDATA._serialized_end=3047
  _DEVICETOTALSIMULATION._serialized_start=3049
  _DEVICETOTALSIMULATION._serialized_end=3103
  _DEVICEOPERATORFLOW._serialized_start=3105
  _DEVICEOPERATORFLOW._serialized_end=3213
  _DEVICEFLOWSETTING._serialized_start=3216
  _DEVICEFLOWSETTING._serialized_end=3349
  _DEVICEOPERATOR._serialized_start=3352
  _DEVICEOPERATOR._serialized_end=3567
  _TASKMGR._serialized_start=3750
  _TASKMGR._serialized_end=3983
# @@protoc_insertion_point(module_scope)
