# Generated by Django 5.0.1 on 2024-02-09 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("group_id", models.IntegerField()),
                ("permission_id", models.IntegerField()),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("content_type_id", models.IntegerField()),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("user_id", models.IntegerField()),
                ("group_id", models.IntegerField()),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("user_id", models.IntegerField()),
                ("permission_id", models.IntegerField()),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
                ("content_type_id", models.IntegerField(blank=True, null=True)),
                ("user_id", models.IntegerField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Constraints",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                (
                    "constraintname",
                    models.CharField(
                        blank=True, db_column="ConstraintName", max_length=45, null=True
                    ),
                ),
                (
                    "image",
                    models.CharField(
                        blank=True, db_column="Image", max_length=50, null=True
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True, db_column="Category", max_length=45, null=True
                    ),
                ),
                (
                    "capacitymax",
                    models.IntegerField(blank=True, db_column="CapacityMax", null=True),
                ),
                (
                    "capacitymin",
                    models.IntegerField(blank=True, db_column="CapacityMin", null=True),
                ),
                (
                    "dischargeloss",
                    models.IntegerField(
                        blank=True, db_column="DischargeLoss", null=True
                    ),
                ),
                (
                    "dischargemax",
                    models.DecimalField(
                        blank=True,
                        db_column="DischargeMax",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "parasiticloss",
                    models.IntegerField(
                        blank=True, db_column="ParasiticLoss", null=True
                    ),
                ),
                (
                    "rampdownmax",
                    models.IntegerField(blank=True, db_column="RampdownMax", null=True),
                ),
                (
                    "rampupmax",
                    models.IntegerField(blank=True, db_column="RampupMax", null=True),
                ),
                (
                    "rechargeloss",
                    models.IntegerField(
                        blank=True, db_column="RechargeLoss", null=True
                    ),
                ),
                (
                    "rechargemax",
                    models.DecimalField(
                        blank=True,
                        db_column="RechargeMax",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "renewable",
                    models.IntegerField(blank=True, db_column="Renewable", null=True),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, db_column="Description", max_length=500, null=True
                    ),
                ),
            ],
            options={
                "db_table": "constraints",
            },
        ),
        migrations.CreateModel(
            name="Genetics",
            fields=[
                (
                    "idgenetics",
                    models.PositiveIntegerField(
                        db_column="idGenetics", primary_key=True, serialize=False
                    ),
                ),
                (
                    "parameter",
                    models.CharField(
                        blank=True, db_column="Parameter", max_length=30, null=True
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        blank=True,
                        db_column="Weight",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "better",
                    models.DecimalField(
                        blank=True,
                        db_column="Better",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "worse",
                    models.DecimalField(
                        blank=True,
                        db_column="Worse",
                        decimal_places=2,
                        max_digits=13,
                        null=True,
                    ),
                ),
                (
                    "minvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="MinValue",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "maxvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="MaxValue",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "step",
                    models.DecimalField(
                        blank=True,
                        db_column="Step",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "betterspinner",
                    models.IntegerField(
                        blank=True, db_column="BetterSpinner", null=True
                    ),
                ),
                (
                    "worsespinner",
                    models.IntegerField(
                        blank=True, db_column="WorseSpinner", null=True
                    ),
                ),
            ],
            options={
                "db_table": "Genetics",
                "db_table_comment": "Parameters used for genetic optimisation",
            },
        ),
        migrations.CreateModel(
            name="Optimisation",
            fields=[
                (
                    "idoptimisation",
                    models.PositiveIntegerField(
                        db_column="idOptimisation", primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, db_column="Name", max_length=45, null=True
                    ),
                ),
                (
                    "approach",
                    models.CharField(
                        blank=True, db_column="Approach", max_length=45, null=True
                    ),
                ),
                (
                    "capacity",
                    models.DecimalField(
                        blank=True,
                        db_column="Capacity",
                        decimal_places=1,
                        max_digits=7,
                        null=True,
                    ),
                ),
                (
                    "capacitymax",
                    models.DecimalField(
                        blank=True,
                        db_column="CapacityMax",
                        decimal_places=1,
                        max_digits=7,
                        null=True,
                    ),
                ),
                (
                    "capacitymin",
                    models.DecimalField(
                        blank=True,
                        db_column="CapacityMin",
                        decimal_places=1,
                        max_digits=7,
                        null=True,
                    ),
                ),
                (
                    "capacitystep",
                    models.DecimalField(
                        blank=True,
                        db_column="CapacityStep",
                        decimal_places=1,
                        max_digits=7,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "Optimisation",
            },
        ),
        migrations.CreateModel(
            name="Scenarios",
            fields=[
                (
                    "idscenarios",
                    models.AutoField(
                        db_column="idScenarios", primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, db_column="Title", max_length=45, null=True
                    ),
                ),
                (
                    "dateexported",
                    models.DateField(blank=True, db_column="DateExported", null=True),
                ),
                (
                    "year",
                    models.SmallIntegerField(blank=True, db_column="Year", null=True),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, db_column="Description", max_length=500, null=True
                    ),
                ),
            ],
            options={
                "db_table": "Scenarios",
            },
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "idsettings",
                    models.PositiveIntegerField(
                        db_column="idSettings", primary_key=True, serialize=False
                    ),
                ),
                ("context", models.CharField(blank=True, max_length=20, null=True)),
                ("parameter", models.CharField(blank=True, max_length=45, null=True)),
                ("value", models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                "db_table": "Settings",
            },
        ),
        migrations.CreateModel(
            name="Stations",
            fields=[
                (
                    "id",
                    models.PositiveIntegerField(
                        db_column="ID", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=45, null=True)),
                ("technology", models.CharField(blank=True, max_length=45, null=True)),
                (
                    "capacity",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "capacityfactor",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "generation",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=9, null=True
                    ),
                ),
                ("transmitted", models.CharField(blank=True, max_length=9, null=True)),
            ],
            options={
                "db_table": "stations",
            },
        ),
        migrations.CreateModel(
            name="Technologies",
            fields=[
                (
                    "idtechnologies",
                    models.AutoField(
                        db_column="idTechnologies", primary_key=True, serialize=False
                    ),
                ),
                (
                    "technology_name",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("image", models.CharField(blank=True, max_length=50, null=True)),
                ("caption", models.CharField(blank=True, max_length=50, null=True)),
                ("category", models.CharField(blank=True, max_length=45, null=True)),
                ("renewable", models.IntegerField(blank=True, null=True)),
                ("dispatchable", models.IntegerField(blank=True, null=True)),
                ("merit_order", models.IntegerField(blank=True, null=True)),
                (
                    "capex",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=9, null=True
                    ),
                ),
                (
                    "fom",
                    models.DecimalField(
                        blank=True,
                        db_column="FOM",
                        decimal_places=0,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "vom",
                    models.DecimalField(
                        blank=True,
                        db_column="VOM",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "lifetime",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=3, null=True
                    ),
                ),
                (
                    "discount_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "Technologies",
            },
        ),
        migrations.CreateModel(
            name="Analysis",
            fields=[
                (
                    "idanalysis",
                    models.AutoField(
                        db_column="idAnalysis", primary_key=True, serialize=False
                    ),
                ),
                (
                    "heading",
                    models.CharField(
                        blank=True, db_column="Heading", max_length=45, null=True
                    ),
                ),
                (
                    "variation",
                    models.CharField(
                        blank=True, db_column="Basis", max_length=45, null=True
                    ),
                ),
                (
                    "stage",
                    models.CharField(
                        blank=True, db_column="Stage", max_length=45, null=True
                    ),
                ),
                (
                    "quantity",
                    models.FloatField(blank=True, db_column="Quantity", null=True),
                ),
                (
                    "units",
                    models.CharField(
                        blank=True, db_column="Units", max_length=10, null=True
                    ),
                ),
                (
                    "idscenarios",
                    models.ForeignKey(
                        blank=True,
                        db_column="idScenarios",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.scenarios",
                    ),
                ),
            ],
            options={
                "db_table": "Analysis",
            },
        ),
        migrations.CreateModel(
            name="Storageattributes",
            fields=[
                (
                    "idstorageattributes",
                    models.AutoField(
                        db_column="idStorageAttributes",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("capacity_max", models.IntegerField(blank=True, null=True)),
                ("capacity_min", models.IntegerField(blank=True, null=True)),
                ("discharge_loss", models.IntegerField(blank=True, null=True)),
                (
                    "discharge_max",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("parasitic_loss", models.IntegerField(blank=True, null=True)),
                ("rampdown_max", models.IntegerField(blank=True, null=True)),
                ("rampup_max", models.IntegerField(blank=True, null=True)),
                ("recharge_loss", models.IntegerField(blank=True, null=True)),
                (
                    "recharge_max",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "idtechnologies",
                    models.ForeignKey(
                        blank=True,
                        db_column="idTechnologies",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.technologies",
                    ),
                ),
            ],
            options={
                "db_table": "StorageAttributes",
            },
        ),
        migrations.CreateModel(
            name="Generatorattributes",
            fields=[
                (
                    "idgeneratorattributes",
                    models.AutoField(
                        db_column="idGeneratorAttributes",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "capacity",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "emissions",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=5, null=True
                    ),
                ),
                (
                    "initial",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("mult", models.FloatField(blank=True, null=True)),
                ("fuel", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "idtechnologies",
                    models.ForeignKey(
                        db_column="idTechnologies",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.technologies",
                    ),
                ),
            ],
            options={
                "db_table": "GeneratorAttributes",
            },
        ),
        migrations.CreateModel(
            name="Zones",
            fields=[
                (
                    "idzones",
                    models.PositiveIntegerField(
                        db_column="idZones", primary_key=True, serialize=False
                    ),
                ),
                (
                    "idscenarios",
                    models.PositiveIntegerField(
                        blank=True, db_column="idScenarios", null=True
                    ),
                ),
                ("existing", models.IntegerField(blank=True, null=True)),
                (
                    "capacity",
                    models.DecimalField(
                        blank=True,
                        db_column="Capacity",
                        decimal_places=2,
                        max_digits=11,
                        null=True,
                    ),
                ),
                (
                    "constraintid",
                    models.ForeignKey(
                        blank=True,
                        db_column="ConstraintID",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.constraints",
                    ),
                ),
            ],
            options={
                "db_table": "Zones",
            },
        ),
        migrations.CreateModel(
            name="Demand",
            fields=[
                (
                    "iddemand",
                    models.PositiveIntegerField(
                        db_column="idDemand", primary_key=True, serialize=False
                    ),
                ),
                ("hour", models.PositiveIntegerField()),
                ("period", models.DateTimeField(blank=True, null=True)),
                (
                    "load",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "col",
                    models.PositiveIntegerField(blank=True, db_column="Col", null=True),
                ),
                (
                    "constraintid",
                    models.ForeignKey(
                        db_column="ConstraintID",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.constraints",
                    ),
                ),
            ],
            options={
                "db_table": "Demand",
                "unique_together": {("iddemand", "constraintid", "hour")},
            },
        ),
        migrations.CreateModel(
            name="Generators",
            fields=[
                (
                    "id",
                    models.PositiveIntegerField(
                        db_column="ID", primary_key=True, serialize=False
                    ),
                ),
                ("year", models.IntegerField(db_column="Year")),
                (
                    "name",
                    models.CharField(
                        blank=True, db_column="Name", max_length=45, null=True
                    ),
                ),
                (
                    "image",
                    models.CharField(
                        blank=True, db_column="Image", max_length=65, null=True
                    ),
                ),
                (
                    "capacity",
                    models.DecimalField(
                        blank=True,
                        db_column="Capacity",
                        decimal_places=2,
                        max_digits=7,
                        null=True,
                    ),
                ),
                (
                    "emissions",
                    models.DecimalField(
                        blank=True,
                        db_column="Emissions",
                        decimal_places=3,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "initial",
                    models.DecimalField(
                        blank=True,
                        db_column="Initial",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                ("ord", models.IntegerField(blank=True, db_column="Ord", null=True)),
                (
                    "dispatchable",
                    models.IntegerField(
                        blank=True, db_column="Dispatchable", null=True
                    ),
                ),
                ("mult", models.FloatField(blank=True, null=True)),
                (
                    "capex",
                    models.DecimalField(
                        blank=True,
                        db_column="Capex",
                        decimal_places=0,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "fom",
                    models.DecimalField(
                        blank=True,
                        db_column="FOM",
                        decimal_places=0,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "vom",
                    models.DecimalField(
                        blank=True,
                        db_column="VOM",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "fuel",
                    models.DecimalField(
                        blank=True,
                        db_column="Fuel",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "lifetime",
                    models.DecimalField(
                        blank=True,
                        db_column="Lifetime",
                        decimal_places=0,
                        max_digits=3,
                        null=True,
                    ),
                ),
                (
                    "discountrate",
                    models.DecimalField(
                        blank=True,
                        db_column="DiscountRate",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "constr",
                    models.ForeignKey(
                        blank=True,
                        db_column="Constr",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.constraints",
                    ),
                ),
            ],
            options={
                "db_table": "generators",
                "unique_together": {("id", "year")},
            },
        ),
    ]
