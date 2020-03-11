"""
Patch for OneLogin_Saml2_XML.validate_xml to suppress XML Schema validation.

This is only required for SAML2 AuthN based Django projects hosted on UW
Standard Managed CentOS6 hosts.

To use this patch, add the repository URL to your requirements.txt file.
"""

from onelogin.saml2.xml_utils import OneLogin_Saml2_XML


def no_validate_xml(xml, schema, debug=False):
    try:
        return OneLogin_Saml2_XML.to_etree(xml)
    except Exception as e:
        if debug:
            print(e)
        return 'unloaded_xml'


OneLogin_Saml2_XML.validate_xml = staticmethod(no_validate_xml)
