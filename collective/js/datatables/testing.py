from plone.testing import z2

from plone.app.testing import *
import collective.js.datatables

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=collective.js.datatables,
                                additional_z2_products=[],
                                gs_profile_id='collective.js.datatables:default',
                                name="collective.js.datatables:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.js.datatables:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.js.datatables:Functional")

