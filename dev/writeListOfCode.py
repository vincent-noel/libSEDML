#!/usr/bin/env python
#
# @file   writeListOfCode.py
# @brief  Create the code for a list of class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions

def writeConstructors(element, package, output):
  element = generalFunctions.writeListOf(element)
  indent = strFunctions.getIndent(element)
  output.write('/*\n' )
  output.write(' * Constructor \n')
  output.write(' */\n')
  output.write('{0}::{0}(unsigned int level, \n'.format(element))
  output.write('\t{0}unsigned int version)\n'.format(indent))
  output.write(' : SedListOf(level, version)\n')
  output.write('{\n' )
  output.write('\tsetSedMLNamespacesAndOwn(new ')
  output.write('SedMLNamespaces(level, version)); \n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Constructor \n')
  output.write(' */\n')
  output.write('{0}::{0}(SedMLNamespaces* {1}ns)\n '.format(element, package.lower()))
  output.write(' : SedListOf({0}ns)\n'.format(package.lower()))
  output.write('{\n' )
  output.write('\tsetElementNamespace({0}ns->getURI());\n'.format(package.lower()))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Returns a deep copy of this {0} \n'.format(element))
  output.write(' */\n')
  output.write('{0}* \n'.format(element))
  output.write('{0}::clone () const\n '.format(element))
  output.write('{\n' )
  output.write('\treturn new {0}(*this);\n'.format(element))
  output.write('}\n\n\n')
  
def writeGetFunctions(output, element, subelement=False, topelement="", name=""):
  listOf = generalFunctions.writeListOf(element)
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write(' */\n')
    output.write('{0}*\n'.format(element))
    output.write('{0}::get{1}(unsigned int n)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(n);\n'.format(name))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by index.\n'.format(element, listOf))
    output.write('*/\n')
    output.write('{0}*\n'.format(element))
    output.write('{0}::get(unsigned int n)\n'.format(listOf))
    output.write('{\n' )
    output.write('\treturn static_cast<{0}*>(SedListOf::get(n));\n'.format(element))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write(' */\n')
    output.write('const {0}*\n'.format(element))
    output.write('{0}::get{1}(unsigned int n) const\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(n);\n'.format(name))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by index.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('const {0}*\n'.format(element))
    output.write('{0}::get(unsigned int n) const\n'.format(listOf))
    output.write('{\n' )
    output.write('\treturn static_cast<const {0}*>(SedListOf::get(n));\n'.format(element))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(element))
    output.write('{0}::get{1}(const std::string& sid)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(sid);\n'.format(name))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(element))
    output.write('{0}::get(const std::string& sid)\n'.format(listOf))
    output.write('{\n' )
    output.write('\treturn const_cast<{0}*>(\n'.format(element))
    output.write('\t  static_cast<const {0}&>(*this).get(sid));\n'.format(listOf))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('const {0}*\n'.format(element))
    output.write('{0}::get{1}(const std::string& sid) const\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(sid);\n'.format(name))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('const {0}*\n'.format(element))
    output.write('{0}::get(const std::string& sid) const\n'.format(listOf))
    output.write('{\n' )
    output.write('\tvector<SedBase*>::const_iterator result;\n\n')
    output.write('\tresult = find_if( mItems.begin(), mItems.end(), IdEq<{0}>(sid) );\n'.format(element))
    output.write('\treturn (result == mItems.end()) ? 0 : static_cast <{0}*> (*result);\n'.format(element))
    output.write('}\n\n\n')
     
def writeRemoveFunctions(output, element, subelement=False, topelement="", name=""):
  listOf = generalFunctions.writeListOf(element)
  output.write('/*\n')
  if subelement == True:
    output.write(' * Removes the nth {0} from the {1}.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(element))
    output.write('{0}::remove{1}(unsigned int n)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.remove(n);\n'.format(name))
    output.write('}\n\n\n')
  else:
    output.write(' * Removes the nth {0} from this {1}\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n{1}::remove(unsigned int n)\n'.format(element, listOf))
    output.write('{\n' )
    output.write('\treturn static_cast<{0}*>(SedListOf::remove(n));\n'.format(element))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Removes the a {0} with given id from the {1}.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(element))
    output.write('{0}::remove{1}(const std::string& sid)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.remove(sid);\n'.format(name))
    output.write('}\n\n\n')
  else:
    output.write(' * Removes the {0} from this {1} with the given identifier\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n{1}::remove(const std::string& sid)\n'.format(element, listOf))
    output.write('{\n' )
    output.write('\tSedBase* item = NULL;\n')
    output.write('\tvector<SedBase*>::iterator result;\n\n')
    output.write('\tresult = find_if( mItems.begin(), mItems.end(), IdEq<{0}>(sid) );\n\n'.format(element))
    output.write('\tif (result != mItems.end())\n\t{\n')
    output.write('\t\titem = *result;\n')
    output.write('\t\tmItems.erase(result);\n\t}\n\n')
    output.write('\treturn static_cast <{0}*> (item);\n'.format(element))
    output.write('}\n\n\n')
     
  
def writeProtectedFunctions(output, element, package, name, elementDict):
  listOf = generalFunctions.writeListOf(element)
  generalFunctions.writeInternalStart(output)
  output.write('/*\n')
  output.write(' * Creates a new {0} in this {1}\n'.format(element, listOf))
  output.write(' */\n')
  output.write('SedBase*\n{0}::createObject(XMLInputStream& stream)\n'.format(listOf))
  output.write('{\n' )
  output.write('\tconst std::string& name   = stream.peek().getName();\n')
  output.write('\tSedBase* object = NULL;\n\n')
  if elementDict == None or elementDict.has_key('abstract') == False or (elementDict.has_key('abstract') and elementDict['abstract'] == False):
    output.write('\tif (name == "{0}")\n'.format(name))
    output.write('\t{\n')
    output.write('\t\tobject = new {0}(getSedMLNamespaces());\n'.format(element))
    output.write('\t\tappendAndOwn(object);\n\t}\n\n')
  elif elementDict != None and elementDict.has_key('concrete'):
    for elem in elementDict['concrete']:
      output.write('\tif (name == "{0}")\n'.format(elem['name']))
      output.write('\t{\n')
      output.write('\t\tobject = new {0}(getSedMLNamespaces());\n'.format(elem['element']))
      output.write('\t\tappendAndOwn(object);\n\t}\n\n')
  output.write('\treturn object;\n')
  output.write('}\n\n\n')
  generalFunctions.writeInternalEnd(output)
  generalFunctions.writeInternalStart(output)
  output.write('/*\n')
  output.write(' * Write the namespace for the {0} package.\n'.format(package))
  output.write(' */\n')
  output.write('void\n{0}::writeXMLNS(XMLOutputStream& stream) const\n'.format(listOf))
  output.write('{\n' )
  output.write('\tXMLNamespaces xmlns;\n\n')
  output.write('\tstd::string prefix = getPrefix();\n\n')
  output.write('\tif (prefix.empty())\n')
  output.write('\t{\n')
  output.write('\t\tif (getNamespaces() != NULL && !getNamespaces()->hasURI(SEDML_XMLNS_L1))\n')
  output.write('\t\t{\n')
  output.write('\t\t\txmlns.add(SEDML_XMLNS_L1,prefix);\n')
  output.write('\t\t}\n')
  output.write('\t}\n\n')
  output.write('\tstream << xmlns;\n')
  output.write('}\n\n\n')
  generalFunctions.writeInternalEnd(output)
  
   
# write the code file      
def createCode(element, code):
  writeConstructors(element['name'], element['package'], code) 
  writeGetFunctions(code, element['name'])
  writeRemoveFunctions(code, element['name'])
  generalFunctions.writeCommonCPPCode(code, element['name'], element['typecode'],None,  True, False,False, element)
  elementName = element['name']
  if element.has_key('elementName'):
    elementName = element['elementName']
  writeProtectedFunctions(code, element['name'], element['package'], elementName, element)

  