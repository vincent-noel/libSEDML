#!/usr/bin/env python
#
# @file   createNewElementDictObj.py
# @brief  Create element object to pass to functions
# @author Sarah Keating
#

import sys

import writeCode
import writeHeader

def createElements():
  element = createSedDocument()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedModel()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedChange()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedParameter()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedVariable()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedChangeAttribute()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedChangeRemoveXML()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedComputeChange()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedSimulation()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedAlgorithm()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedTask()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedDataGenerator()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createSedOutput()
  writeCode.createCode(element)
  writeHeader.createHeader(element)

def createSedDocument() :
  a1 = dict({'type': 'int', 'reqd' : True, 'name':'level'})
  a2 = dict({'type': 'int', 'reqd' : True, 'name':'version'})
  lo1 = dict({'type': 'lo_element', 'reqd' : False, 'name':'model', 'element': 'SedMLModel'})
  lo2 = dict({'type': 'lo_element', 'reqd' : False, 'name':'simulation', 'element': 'Simulation'})
  lo3 = dict({'type': 'lo_element', 'reqd' : False, 'name':'task', 'element': 'Task'})
  lo4 = dict({'type': 'lo_element', 'reqd' : False, 'name':'dataGenerator', 'element': 'DataGenerator'})
  lo5 = dict({'type': 'lo_element', 'reqd' : False, 'name':'output', 'element': 'Output'})
  attributes = [a1, a2, lo1, lo2, lo3, lo4, lo5]
  element = dict({'name': 'SedMLDocument', 'package': 'SedML', 'typecode': 'SEDML_DOCUMENT', 'hasSedListOf': False, 'attribs':attributes, 'hasChildren':True, 'hasMath':False, 'elementName':'sedML'}) 
  return element

def createSedModel() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  a3 = dict({'type': 'string', 'reqd' : False, 'name':'language'})
  a4 = dict({'type': 'string', 'reqd' : True, 'name':'source'})
  lo1 = dict({'type': 'lo_element', 'reqd' : False, 'name':'change', 'element': 'Change'})
  attributes = [a1, a2, a3, a4, lo1]
  element = dict({'name': 'SedMLModel', 'package': 'SedML', 'typecode': 'SEDML_MODEL', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False, 'elementName':'model'}) 
  return element

def createSedVariable() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  a3 = dict({'type': 'string', 'reqd' : False, 'name':'symbol'})
  a4 = dict({'type': 'string', 'reqd' : False, 'name':'target'})
  a5 = dict({'type': 'SIdRef', 'reqd' : False, 'name':'taskReference'})
  a6 = dict({'type': 'SIdRef', 'reqd' : False, 'name':'modelReference'})
  attributes = [a1, a2, a3, a4, a5, a6]
  element = dict({'name': 'SedMLVariable', 'package': 'SedML', 'typecode': 'SEDML_VARIABLE', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False, 'elementName':'variable'}) 
  return element

def createSedParameter() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  a3 = dict({'type': 'double', 'reqd' : True, 'name':'value'})
  attributes = [a1, a2, a3]
  element = dict({'name': 'SedMLParameter', 'package': 'SedML', 'typecode': 'SEDML_PARAMETER', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False, 'elementName':'parameter'}) 
  return element

def createSedAlgorithm() :
  a1 = dict({'type': 'string', 'reqd' : True, 'name':'kisaoID'})
  attributes = [a1]
  element = dict({'name': 'Algorithm', 'package': 'SedML', 'typecode': 'SEDML_SIMULATION_ALGORITHM', 'hasSedListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element
  
def createSedChange() :
  a1 = dict({'type': 'string', 'reqd' : True, 'name':'target'})
  attributes = [a1]
  element = dict({'name': 'Change', 'package': 'SedML', 'typecode': 'SEDML_CHANGE', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False, 'elementName':'change'}) 
  return element

def createSedChangeRemoveXML() :
  attributes = []
  element = dict({'name': 'RemoveXML', 'package': 'SedML', 'typecode': 'SEDML_CHANGE_REMOVEXML', 'hasSedListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False, 'baseClass':'Change'}) 
  return element

def createSedComputeChange() :
  lo1 = dict({'type': 'lo_element', 'reqd' : False, 'name':'variable', 'element': 'SedMLVariable'})
  lo2 = dict({'type': 'lo_element', 'reqd' : False, 'name':'parameter', 'element': 'SedMLParameter'})
  a1 = dict({'type': 'element', 'reqd' : False, 'name':'math'})
  attributes = [lo1, lo2, a1]
  element = dict({'name': 'ComputeChange', 'package': 'SedML', 'typecode': 'SEDML_CHANGE_COMPUTECHANGE', 'hasSedListOf': False, 'attribs':attributes, 'hasChildren':True, 'hasMath':True, 'baseClass':'Change'}) 
  return element

def createSedChangeAttribute() :
  a1 = dict({'type': 'string', 'reqd' : True, 'name':'newValue'})
  attributes = [a1]
  element = dict({'name': 'ChangeAttribute', 'package': 'SedML', 'typecode': 'SEDML_CHANGE_ATTRIBUTE', 'hasSedListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False, 'baseClass':'Change'}) 
  return element
  
def createSedSimulation() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  a3 = dict({'type': 'element', 'reqd' : False, 'name':'algorithm'})
  attributes = [a1, a2, a3]
  element = dict({'name': 'Simulation', 'package': 'SedML', 'typecode': 'SEDML_SIMULATION', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element

def createSedTask() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  attributes = [a1, a2]
  element = dict({'name': 'Task', 'package': 'SedML', 'typecode': 'SEDML_TASK', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element

def createSedDataGenerator() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  lo1 = dict({'type': 'lo_element', 'reqd' : False, 'name':'variable', 'element': 'SedMLVariable'})
  lo2 = dict({'type': 'lo_element', 'reqd' : False, 'name':'parameter', 'element': 'SedMLParameter'})
  a3 = dict({'type': 'element', 'reqd' : False, 'name':'math'})
  attributes = [a1, a2, lo1, lo2, a3]
  element = dict({'name': 'DataGenerator', 'package': 'SedML', 'typecode': 'SEDML_DATAGENERATOR', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':True}) 
  return element

def createSedOutput() :
  a1 = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  a2 = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  attributes = [a1, a2]
  element = dict({'name': 'Output', 'package': 'SedML', 'typecode': 'SEDML_OUTPUT', 'hasSedListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element
  
  
