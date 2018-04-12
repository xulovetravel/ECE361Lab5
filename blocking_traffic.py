import ryu_ofctl
flow=ryu_ofctl.FlowEntry()
act1=ryu_ofctl.OutputAction(3)
act2=ryu_ofctl.OutputAction(2)
flow.in_port=1
flow.addAction(act1)
flow.addAction(act2)
dpid=1
ryu_ofctl.insertFlow(dpid,flow)
flow.in_port=1
ryu_ofctl.deleteFlow(dpid,flow)
flow.in_port=3
ryu_ofctl.deleteFlow(dpid,flow)
ryu_ofctl.deleteAllFlows(dpid)
dpid=1
ryu_ofctl.insertFlow(dpid,flow)
