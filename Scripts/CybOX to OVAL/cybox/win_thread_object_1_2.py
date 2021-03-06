#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Apr 10 13:54:59 2012 by generateDS.py version 2.7b.
#

import sys
import getopt
import re as re_
import common_types_1_0 as common
import win_handle_object_1_2 as win_handle_object

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace,name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class WindowsThreadObjectType(common.DefinedObjectType):
    """The Windows_ThreadObjectType is intended to characterize Windows
    process threads. See also: http://msdn.microsoft.com/en-
    us/library/windows/desktop/ms684852(v=vs.85).aspx"""
    subclass = None
    superclass = common.DefinedObjectType
    def __init__(self, Thread_ID=None, Handle=None, Running_Status=None, Context=None, Priority=None, Creation_Flags=None, Creation_Time=None, Start_Address=None, Parameter_Address=None, Security_Attributes=None, Stack_Size=None):
        super(WindowsThreadObjectType, self).__init__(None)
        self.Thread_ID = Thread_ID
        self.Handle = Handle
        self.Running_Status = Running_Status
        self.Context = Context
        self.Priority = Priority
        self.Creation_Flags = Creation_Flags
        self.Creation_Time = Creation_Time
        self.Start_Address = Start_Address
        self.Parameter_Address = Parameter_Address
        self.Security_Attributes = Security_Attributes
        self.Stack_Size = Stack_Size
    def factory(*args_, **kwargs_):
        if WindowsThreadObjectType.subclass:
            return WindowsThreadObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsThreadObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Thread_ID(self): return self.Thread_ID
    def set_Thread_ID(self, Thread_ID): self.Thread_ID = Thread_ID
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def get_Running_Status(self): return self.Running_Status
    def set_Running_Status(self, Running_Status): self.Running_Status = Running_Status
    def validate_ThreadRunningStatusType(self, value):
        # Validate type ThreadRunningStatusType, a restriction on None.
        pass
    def get_Context(self): return self.Context
    def set_Context(self, Context): self.Context = Context
    def get_Priority(self): return self.Priority
    def set_Priority(self, Priority): self.Priority = Priority
    def get_Creation_Flags(self): return self.Creation_Flags
    def set_Creation_Flags(self, Creation_Flags): self.Creation_Flags = Creation_Flags
    def get_Creation_Time(self): return self.Creation_Time
    def set_Creation_Time(self, Creation_Time): self.Creation_Time = Creation_Time
    def get_Start_Address(self): return self.Start_Address
    def set_Start_Address(self, Start_Address): self.Start_Address = Start_Address
    def get_Parameter_Address(self): return self.Parameter_Address
    def set_Parameter_Address(self, Parameter_Address): self.Parameter_Address = Parameter_Address
    def get_Security_Attributes(self): return self.Security_Attributes
    def set_Security_Attributes(self, Security_Attributes): self.Security_Attributes = Security_Attributes
    def get_Stack_Size(self): return self.Stack_Size
    def set_Stack_Size(self, Stack_Size): self.Stack_Size = Stack_Size
    def export(self, outfile, level, namespace_='WinThreadObj:', name_='WindowsThreadObjectType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsThreadObjectType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, 'WinThreadObj:', name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinThreadObj:', name_='WindowsThreadObjectType'):
        super(WindowsThreadObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsThreadObjectType')
    def exportChildren(self, outfile, level, namespace_='WinThreadObj:', name_='WindowsThreadObjectType', fromsubclass_=False):
        if self.Thread_ID is not None:
            self.Thread_ID.export(outfile, level, namespace_, name_='Thread_ID')
        if self.Handle is not None:
            self.Handle.export(outfile, level, namespace_, name_='Handle')
        if self.Running_Status is not None:
            self.Running_Status.export(outfile, level, namespace_, name_='Running_Status')
        if self.Context is not None:
            self.Context.export(outfile, level, namespace_, name_='Context')
        if self.Priority is not None:
            self.Priority.export(outfile, level, namespace_, name_='Priority')
        if self.Creation_Flags is not None:
            self.Creation_Flags.export(outfile, level, namespace_, name_='Creation_Flags')
        if self.Creation_Time is not None:
            self.Creation_Time.export(outfile, level, namespace_, name_='Creation_Time')
        if self.Start_Address is not None:
            self.Start_Address.export(outfile, level, namespace_, name_='Start_Address')
        if self.Parameter_Address is not None:
            self.Parameter_Address.export(outfile, level, namespace_, name_='Parameter_Address')
        if self.Security_Attributes is not None:
            self.Security_Attributes.export(outfile, level, namespace_, name_='Security_Attributes')
        if self.Stack_Size is not None:
            self.Stack_Size.export(outfile, level, namespace_, name_='Stack_Size')
    def hasContent_(self):
        if (
            self.Thread_ID is not None or
            self.Handle is not None or
            self.Running_Status is not None or
            self.Context is not None or
            self.Priority is not None or
            self.Creation_Flags is not None or
            self.Creation_Time is not None or
            self.Start_Address is not None or
            self.Parameter_Address is not None or
            self.Security_Attributes is not None or
            self.Stack_Size is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='WindowsThreadObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Thread_ID is not None:
            showIndent(outfile, level)
            outfile.write('Thread_ID=%s,\n' % quote_python(self.Thread_ID).encode(ExternalEncoding))
        if self.Handle is not None:
            showIndent(outfile, level)
            outfile.write('Handle=%s,\n' % quote_python(self.Handle).encode(ExternalEncoding))
        if self.Running_Status is not None:
            showIndent(outfile, level)
            outfile.write('Running_Status=model_.ThreadRunningStatusType(\n')
            self.Running_Status.exportLiteral(outfile, level, name_='Running_Status')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Context is not None:
            showIndent(outfile, level)
            outfile.write('Context=%s,\n' % quote_python(self.Context).encode(ExternalEncoding))
        if self.Priority is not None:
            showIndent(outfile, level)
            outfile.write('Priority=%s,\n' % quote_python(self.Priority).encode(ExternalEncoding))
        if self.Creation_Flags is not None:
            showIndent(outfile, level)
            outfile.write('Creation_Flags=%s,\n' % quote_python(self.Creation_Flags).encode(ExternalEncoding))
        if self.Creation_Time is not None:
            showIndent(outfile, level)
            outfile.write('Creation_Time=%s,\n' % quote_python(self.Creation_Time).encode(ExternalEncoding))
        if self.Start_Address is not None:
            showIndent(outfile, level)
            outfile.write('Start_Address=%s,\n' % quote_python(self.Start_Address).encode(ExternalEncoding))
        if self.Parameter_Address is not None:
            showIndent(outfile, level)
            outfile.write('Parameter_Address=%s,\n' % quote_python(self.Parameter_Address).encode(ExternalEncoding))
        if self.Security_Attributes is not None:
            showIndent(outfile, level)
            outfile.write('Security_Attributes=%s,\n' % quote_python(self.Security_Attributes).encode(ExternalEncoding))
        if self.Stack_Size is not None:
            showIndent(outfile, level)
            outfile.write('Stack_Size=%s,\n' % quote_python(self.Stack_Size).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Thread_ID':
            Thread_ID_ = child_.text
            Thread_ID_ = self.gds_validate_string(Thread_ID_, node, 'Thread_ID')
            self.Thread_ID = Thread_ID_
        elif nodeName_ == 'Handle':
            Handle_ = child_.text
            Handle_ = self.gds_validate_string(Handle_, node, 'Handle')
            self.Handle = Handle_
        elif nodeName_ == 'Running_Status':
            obj_ = None
            self.set_Running_Status(obj_)
            self.validate_ThreadRunningStatusType(self.Running_Status)    # validate type ThreadRunningStatusType
        elif nodeName_ == 'Context':
            Context_ = child_.text
            Context_ = self.gds_validate_string(Context_, node, 'Context')
            self.Context = Context_
        elif nodeName_ == 'Priority':
            Priority_ = child_.text
            Priority_ = self.gds_validate_string(Priority_, node, 'Priority')
            self.Priority = Priority_
        elif nodeName_ == 'Creation_Flags':
            Creation_Flags_ = child_.text
            Creation_Flags_ = self.gds_validate_string(Creation_Flags_, node, 'Creation_Flags')
            self.Creation_Flags = Creation_Flags_
        elif nodeName_ == 'Creation_Time':
            Creation_Time_ = child_.text
            Creation_Time_ = self.gds_validate_string(Creation_Time_, node, 'Creation_Time')
            self.Creation_Time = Creation_Time_
        elif nodeName_ == 'Start_Address':
            Start_Address_ = child_.text
            Start_Address_ = self.gds_validate_string(Start_Address_, node, 'Start_Address')
            self.Start_Address = Start_Address_
        elif nodeName_ == 'Parameter_Address':
            Parameter_Address_ = child_.text
            Parameter_Address_ = self.gds_validate_string(Parameter_Address_, node, 'Parameter_Address')
            self.Parameter_Address = Parameter_Address_
        elif nodeName_ == 'Security_Attributes':
            Security_Attributes_ = child_.text
            Security_Attributes_ = self.gds_validate_string(Security_Attributes_, node, 'Security_Attributes')
            self.Security_Attributes = Security_Attributes_
        elif nodeName_ == 'Stack_Size':
            Stack_Size_ = child_.text
            Stack_Size_ = self.gds_validate_string(Stack_Size_, node, 'Stack_Size')
            self.Stack_Size = Stack_Size_
        super(WindowsThreadObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsThreadObjectType


class ThreadRunningStatusType(GeneratedsSuper):
    """ThreadRunningStatusType specifies Windows thread running states via
    a union of the ThreadRunningStatusEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    BaseObjectAttributeType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    element."""
    subclass = None
    superclass = None
    def __init__(self, datatype=None, valueOf_=None):
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ThreadRunningStatusType.subclass:
            return ThreadRunningStatusType.subclass(*args_, **kwargs_)
        else:
            return ThreadRunningStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='WinThreadObj:', name_='ThreadRunningStatusType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ThreadRunningStatusType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinThreadObj:', name_='ThreadRunningStatusType'):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            outfile.write(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, outfile, level, namespace_='WinThreadObj:', name_='ThreadRunningStatusType', fromsubclass_=False):
        pass
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ThreadRunningStatusType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            showIndent(outfile, level)
            outfile.write('datatype = %s,\n' % (self.datatype,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            self.datatype = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ThreadRunningStatusType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Thread'
        rootClass = WindowsThreadObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag, 
        namespacedef_='')
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Thread'
        rootClass = WindowsThreadObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Windows_Thread",
        namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Thread'
        rootClass = WindowsThreadObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from Win_Thread_Object import *\n\n')
    sys.stdout.write('import Win_Thread_Object as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


__all__ = [
    "ThreadRunningStatusType",
    "WindowsThreadObjectType"
    ]
