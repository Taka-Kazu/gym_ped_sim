#!/usr/bin/env python
# coding=utf-8

from lxml import etree
from lxml.etree import Element


def get_actor_collisions_plugin_element():
    actor_collisions_plugin_element = etree.fromstring('\
<?xml version="1.0"?>\
<plugin name="actor_collisions_plugin" filename="libActorCollisionsPlugin.so">\
<scaling collision="LHipJoint_LeftUpLeg_collision" scale="\
0.01 \
0.001 \
0.001\
"/>\
<scaling collision="LeftUpLeg_LeftLeg_collision" scale="\
8.0 \
8.0 \
1.0 \
"/>\
<scaling collision="LeftLeg_LeftFoot_collision" scale="\
8.0 \
8.0 \
1.0\
"/>\
<scaling collision="LeftFoot_LeftToeBase_collision" scale="\
4.0 \
4.0 \
1.5 \
"/>\
<scaling collision="RHipJoint_RightUpLeg_collision" scale="\
0.01 \
0.001 \
0.001\
"/>\
<scaling collision="RightUpLeg_RightLeg_collision" scale="\
8.0 \
8.0 \
1.0\
"/>\
<scaling collision="RightLeg_RightFoot_collision" scale="\
8.0 \
8.0 \
1.0\
"/>\
<scaling collision="RightFoot_RightToeBase_collision" scale="\
4.0 \
4.0 \
1.5\
"/>\
<scaling collision="LowerBack_Spine_collision" scale="\
12.0 \
20.0 \
5.0\
" pose="0.05 0 0 0 -0.2 0"/>\
<scaling collision="Spine_Spine1_collision" scale="\
0.01 \
0.001 \
0.001\
"/>\
<scaling collision="Neck_Neck1_collision" scale="\
0.01 \
0.001 \
0.001\
"/>\
<scaling collision="Neck1_Head_collision" scale="\
5.0 \
5.0 \
3.0\
"/>\
<scaling collision="LeftShoulder_LeftArm_collision" scale="\
0.01 \
0.001 \
0.001\
"/>\
<scaling collision="LeftArm_LeftForeArm_collision" scale="\
5.0 \
5.0 \
1.0\
"/>\
<scaling collision="LeftForeArm_LeftHand_collision" scale="\
5.0 \
5.0 \
1.0\
"/>\
<scaling collision="LeftFingerBase_LeftHandIndex1_collision" scale="\
4.0 \
4.0 \
3.0\
"/>\
<scaling collision="RightShoulder_RightArm_collision" scale="\
0.01 \
0.001 \
0.001\
"/>\
<scaling collision="RightArm_RightForeArm_collision" scale="\
5.0 \
5.0 \
1.0\
"/>\
<scaling collision="RightForeArm_RightHand_collision" scale="\
5.0 \
5.0 \
1.0\
"/>\
<scaling collision="RightFingerBase_RightHandIndex1_collision" scale="\
4.0 \
4.0 \
3.0\
"/>\
</plugin>\
')
    return actor_collisions_plugin_element
