from django.db import models


# DB Model for a Category -> Unique name, Description, creation date, last modified date
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=120)
    category_Description = models.CharField(max_length=300)
    date_Created = models.DateTimeField(auto_now_add=True)
    last_Modified = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'Category: {}'.format(self.category_name)

    def __unicode__(self):
       return 'Category: ' + self.category_name

# DB Model for a Workflow -> Unique name, Description, # of Steps, creation date, last modified date
class Workflow(models.Model):

    id = models.AutoField(primary_key=True)
    #Each workflow must be assigned to one or more categories
    category = models.ForeignKey(Category) ### This also creates a category_id column automatically!

    workflow_name = models.CharField(max_length=120)
    workflow_Description = models.CharField(max_length=300)
    workflow_Steps = models.IntegerField()
    date_Created = models.DateTimeField(auto_now_add=True)
    last_Modified = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Workflow, self).__init__(*args, **kwargs)

    def __repr__(self):
        #account for the pluralization of the word "Step"
        if (self.workflow_Steps > 1):
            return 'Workflow: {} [{} Steps] \n\n {}'.format(self.workflow_name, self.workflow_Steps, self.workflow_Description)
        else:
            return 'Workflow: {} [{} Step] \n\n {}'.format(self.workflow_Description, self.workflow_Steps, self.workflow_Description)
    def __unicode__(self):
        if (self.workflow_Steps > 1):
            return 'Workflow: ' + self.workflow_name + " [" + str(self.workflow_Steps) + " Steps]"
        else:
            return 'Workflow: ' + self.workflow_name + " [" + str(self.workflow_Steps) + " Step]"