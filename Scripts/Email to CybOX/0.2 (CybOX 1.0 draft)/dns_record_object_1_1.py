#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Nov 06 14:02:28 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import cybox_common_types_1_0
import uri_object_1_2
import address_object_1_2

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

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
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
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
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

class DNSRecordObjectType(cybox_common_types_1_0.DefinedObjectType):
    """The DNSRecordObjectType type is intended to characterize an
    individual DNS record."""
    subclass = None
    superclass = cybox_common_types_1_0.DefinedObjectType
    def __init__(self, object_reference=None, Description=None, Domain_Name=None, IP_Address=None, Address_Class=None, Entry_Type=None, Record_Name=None, Record_Type=None, TTL=None, Flags=None, Data_Length=None, Record_Data=None):
        super(DNSRecordObjectType, self).__init__(object_reference, )
        self.Description = Description
        self.Domain_Name = Domain_Name
        self.IP_Address = IP_Address
        self.Address_Class = Address_Class
        self.Entry_Type = Entry_Type
        self.Record_Name = Record_Name
        self.Record_Type = Record_Type
        self.TTL = TTL
        self.Flags = Flags
        self.Data_Length = Data_Length
        self.Record_Data = Record_Data
    def factory(*args_, **kwargs_):
        if DNSRecordObjectType.subclass:
            return DNSRecordObjectType.subclass(*args_, **kwargs_)
        else:
            return DNSRecordObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Domain_Name(self): return self.Domain_Name
    def set_Domain_Name(self, Domain_Name): self.Domain_Name = Domain_Name
    def get_IP_Address(self): return self.IP_Address
    def set_IP_Address(self, IP_Address): self.IP_Address = IP_Address
    def get_Address_Class(self): return self.Address_Class
    def set_Address_Class(self, Address_Class): self.Address_Class = Address_Class
    def validate_StringObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.StringObjectAttributeType, a restriction on None.
        pass
    def get_Entry_Type(self): return self.Entry_Type
    def set_Entry_Type(self, Entry_Type): self.Entry_Type = Entry_Type
    def get_Record_Name(self): return self.Record_Name
    def set_Record_Name(self, Record_Name): self.Record_Name = Record_Name
    def get_Record_Type(self): return self.Record_Type
    def set_Record_Type(self, Record_Type): self.Record_Type = Record_Type
    def get_TTL(self): return self.TTL
    def set_TTL(self, TTL): self.TTL = TTL
    def validate_IntegerObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.IntegerObjectAttributeType, a restriction on None.
        pass
    def get_Flags(self): return self.Flags
    def set_Flags(self, Flags): self.Flags = Flags
    def validate_HexBinaryObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.HexBinaryObjectAttributeType, a restriction on None.
        pass
    def get_Data_Length(self): return self.Data_Length
    def set_Data_Length(self, Data_Length): self.Data_Length = Data_Length
    def get_Record_Data(self): return self.Record_Data
    def set_Record_Data(self, Record_Data): self.Record_Data = Record_Data
    def export(self, outfile, level, namespace_='DNSRecordObj:', name_='DNSRecordObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DNSRecordObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='DNSRecordObj:', name_='DNSRecordObjectType'):
        super(DNSRecordObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DNSRecordObjectType')
    def exportChildren(self, outfile, level, namespace_='DNSRecordObj:', name_='DNSRecordObjectType', fromsubclass_=False, pretty_print=True):
        super(DNSRecordObjectType, self).exportChildren(outfile, level, 'DNSRecordObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'DNSRecordObj:', name_='Description', pretty_print=pretty_print)
        if self.Domain_Name is not None:
            self.Domain_Name.export(outfile, level, 'DNSRecordObj:', name_='Domain_Name', pretty_print=pretty_print)
        if self.IP_Address is not None:
            self.IP_Address.export(outfile, level, 'DNSRecordObj:', name_='IP_Address', pretty_print=pretty_print)
        if self.Address_Class is not None:
            self.Address_Class.export(outfile, level, 'DNSRecordObj:', name_='Address_Class', pretty_print=pretty_print)
        if self.Entry_Type is not None:
            self.Entry_Type.export(outfile, level, 'DNSRecordObj:', name_='Entry_Type', pretty_print=pretty_print)
        if self.Record_Name is not None:
            self.Record_Name.export(outfile, level, 'DNSRecordObj:', name_='Record_Name', pretty_print=pretty_print)
        if self.Record_Type is not None:
            self.Record_Type.export(outfile, level, 'DNSRecordObj:', name_='Record_Type', pretty_print=pretty_print)
        if self.TTL is not None:
            self.TTL.export(outfile, level, 'DNSRecordObj:', name_='TTL', pretty_print=pretty_print)
        if self.Flags is not None:
            self.Flags.export(outfile, level, 'DNSRecordObj:', name_='Flags', pretty_print=pretty_print)
        if self.Data_Length is not None:
            self.Data_Length.export(outfile, level, 'DNSRecordObj:', name_='Data_Length', pretty_print=pretty_print)
        if self.Record_Data is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRecord_Data>%s</%sRecord_Data>%s' % ('DNSRecordObj:', self.gds_format_string(quote_xml(self.Record_Data).encode(ExternalEncoding), input_name='Record_Data'), 'DNSRecordObj:', eol_))
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Domain_Name is not None or
            self.IP_Address is not None or
            self.Address_Class is not None or
            self.Entry_Type is not None or
            self.Record_Name is not None or
            self.Record_Type is not None or
            self.TTL is not None or
            self.Flags is not None or
            self.Data_Length is not None or
            self.Record_Data is not None or
            super(DNSRecordObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DNSRecordObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DNSRecordObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DNSRecordObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Domain_Name is not None:
            showIndent(outfile, level)
            outfile.write('Domain_Name=model_.uri_object_1_2.URIObjectType(\n')
            self.Domain_Name.exportLiteral(outfile, level, name_='Domain_Name')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.IP_Address is not None:
            showIndent(outfile, level)
            outfile.write('IP_Address=model_.address_object_1_2.AddressObjectType(\n')
            self.IP_Address.exportLiteral(outfile, level, name_='IP_Address')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Address_Class is not None:
            showIndent(outfile, level)
            outfile.write('Address_Class=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Address_Class.exportLiteral(outfile, level, name_='Address_Class')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Entry_Type is not None:
            showIndent(outfile, level)
            outfile.write('Entry_Type=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Entry_Type.exportLiteral(outfile, level, name_='Entry_Type')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Record_Name is not None:
            showIndent(outfile, level)
            outfile.write('Record_Name=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Record_Name.exportLiteral(outfile, level, name_='Record_Name')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Record_Type is not None:
            showIndent(outfile, level)
            outfile.write('Record_Type=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Record_Type.exportLiteral(outfile, level, name_='Record_Type')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.TTL is not None:
            showIndent(outfile, level)
            outfile.write('TTL=model_.cybox_common_types_1_0.IntegerObjectAttributeType(\n')
            self.TTL.exportLiteral(outfile, level, name_='TTL')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Flags is not None:
            showIndent(outfile, level)
            outfile.write('Flags=model_.cybox_common_types_1_0.HexBinaryObjectAttributeType(\n')
            self.Flags.exportLiteral(outfile, level, name_='Flags')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Data_Length is not None:
            showIndent(outfile, level)
            outfile.write('Data_Length=model_.cybox_common_types_1_0.IntegerObjectAttributeType(\n')
            self.Data_Length.exportLiteral(outfile, level, name_='Data_Length')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Record_Data is not None:
            showIndent(outfile, level)
            outfile.write('Record_Data=%s,\n' % quote_python(self.Record_Data).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DNSRecordObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Domain_Name':
            obj_ = uri_object_1_2.URIObjectType.factory()
            obj_.build(child_)
            self.set_Domain_Name(obj_)
        elif nodeName_ == 'IP_Address':
            obj_ = address_object_1_2.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Address(obj_)
        elif nodeName_ == 'Address_Class':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Address_Class(obj_)
        elif nodeName_ == 'Entry_Type':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Entry_Type(obj_)
        elif nodeName_ == 'Record_Name':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Record_Name(obj_)
        elif nodeName_ == 'Record_Type':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Record_Type(obj_)
        elif nodeName_ == 'TTL':
            obj_ = cybox_common_types_1_0.IntegerObjectAttributeType.factory()
            obj_.build(child_)
            self.set_TTL(obj_)
        elif nodeName_ == 'Flags':
            obj_ = cybox_common_types_1_0.HexBinaryObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Flags(obj_)
        elif nodeName_ == 'Data_Length':
            obj_ = cybox_common_types_1_0.IntegerObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Data_Length(obj_)
        elif nodeName_ == 'Record_Data':
            Record_Data_ = child_.text
            Record_Data_ = self.gds_validate_string(Record_Data_, node, 'Record_Data')
            self.Record_Data = Record_Data_
        super(DNSRecordObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class DNSRecordObjectType

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
        rootTag = 'DNS_Record'
        rootClass = DNSRecordObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DNS_Record'
        rootClass = DNSRecordObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="DNS_Record",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DNS_Record'
        rootClass = DNSRecordObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
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
    "DNSRecordObjectType"
    ]