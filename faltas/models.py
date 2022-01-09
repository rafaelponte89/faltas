# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Afastamentos(models.Model):
    sigla = models.CharField(primary_key=True, max_length=3)
    afastamento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afastamentos'


class AfastamentosProfessores(models.Model):
    prof = models.ForeignKey('Professores', models.DO_NOTHING)
    data_in = models.DateField(primary_key=True)
    data_fn = models.DateField(blank=True, null=True)
    aulas = models.IntegerField(blank=True, null=True)
    sigla = models.ForeignKey(Afastamentos, models.DO_NOTHING, db_column='sigla')
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afastamentos_professores'
        unique_together = (('data_in', 'prof'),)


class Anos(models.Model):
    ano = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'anos'


class Cargos(models.Model):
    carg_id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cargos'


class Disciplinas(models.Model):
    disc_id = models.AutoField(primary_key=True)
    disciplina = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'disciplinas'


class Jornadas(models.Model):
    jorn_id = models.AutoField(primary_key=True)
    jornada = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jornadas'


class Professores(models.Model):
    prof_id = models.IntegerField(primary_key=True)
    professor = models.CharField(max_length=100, blank=True, null=True)
    carg = models.ForeignKey(Cargos, models.DO_NOTHING, blank=True, null=True)
    disc = models.ForeignKey(Disciplinas, models.DO_NOTHING, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    efetivo = models.CharField(max_length=1, blank=True, null=True)
    sede = models.ForeignKey('Sedes', models.DO_NOTHING, blank=True, null=True)
    adm = models.DateField(blank=True, null=True)
    desl = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professores'


class ProfessoresAulas(models.Model):
    prof = models.OneToOneField(Professores, models.DO_NOTHING, primary_key=True)
    jorn = models.ForeignKey(Jornadas, models.DO_NOTHING, blank=True, null=True)
    ano = models.ForeignKey(Anos, models.DO_NOTHING, db_column='ano')
    ha_al = models.IntegerField(blank=True, null=True)
    ha_htp = models.IntegerField(blank=True, null=True)
    supl = models.IntegerField(blank=True, null=True)
    outr = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    faul = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professores_aulas'
        unique_together = (('prof', 'ano'),)


class Sedes(models.Model):
    sede_id = models.CharField(primary_key=True, max_length=6)
    sede = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sedes'
