import ryu_ofctl
flow=ryu_ofctl.FlowEntry()
act=ryu_ofctl.OutputAction(2)
flow.in_port=1
flow.dl_dst="00:00:00:00:00:02"
flow.addAction(act)
dpid2=1
ryu_ofctl.insertFlow(dpid2,flow)
act1=ryu_ofctl.OutputAction(1)
act2=ryu_ofctl.OutputAction(3)
flow.in_port=2
flow.addAction(act2)
flow.addAction(act1)
dpid3=1
ryu_ofctl.insertFlow(dpid3,flow)
