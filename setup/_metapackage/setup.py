import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-quality-control",
    description="Meta package for open-synergy-ssi-quality-control Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_quality_control',
        'odoo14-addon-ssi_quality_control_reference_document',
        'odoo14-addon-ssi_quality_control_related_attachment',
        'odoo14-addon-ssi_quality_control_work_log',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
