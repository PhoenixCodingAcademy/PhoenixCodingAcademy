<title>Data</title>

Terms like table, column, row, record, class, object, property, attribute, field, member, key, and value show up in all sorts of data contexts, like data science, databases, data architectures, and object-oriented programming. Most of these are synonyms so don't think they mean different things.

| Context                | Class Collection   | Class                | Object                        | Property                     | Value                   |
| ---------------------- | ------------------ | -------------------- | ----------------------------- | ---------------------------- | ----------------------- |
| **Databases**          | Database           | Table                | Record, Row                   | Column                       | Cell, Value             |
| **Math**               | Set of sets        | Set                  | Element, Member               | Property                     | Value                   |
| **Object Programming** | Application        | Class                | Object                        | Member, Property, Attribute  | Value                   |
| **Data Science/ML**    | Dataset collection | Dataset              | Observation, Sample, Instance | Feature, Variable, Dimension | Measurement, Data point |
| **Statistics**         | Population         | Distribution/Model   | Case, Unit                    | Variable, Covariate          | Observation, Score      |
| **JSON/NoSQL**         | Database           | Collection           | Document                      | Key, Field                   | Value                   |
| **XML**                | Schema set         | Schema/DTD           | Element, Node                 | Attribute, Tag               | Content, Text           |
| **Spreadsheets**       | Workbook           | Sheet/Table          | Row                           | Column, Field                | Cell value              |
| **Graph Theory**       | Graph collection   | Graph                | Node, Vertex                  | Property, Attribute          | Property value          |
| **Ontologies/RDF**     | Ontology           | Class, Concept       | Individual, Instance          | Property, Predicate          | Object, Literal         |
| **File Systems**       | File system        | Directory            | File                          | Metadata field               | Metadata value          |
| **Business/ERP**       | System             | Entity type          | Entity instance               | Attribute, Field             | Attribute value         |
| **Data Warehousing**   | Data warehouse     | Dimension/Fact table | Fact, Member                  | Attribute, Measure           | Value, Metric           |
| **APIs/REST**          | API                | Resource type        | Resource                      | Property, Field              | Value                   |
| **Knowledge Graphs**   | Knowledge base     | Entity type          | Entity                        | Relation, Property           | Triple object           |
| **Computer Vision**    | Image dataset      | Image class          | Image                         | Pixel, Channel               | Intensity, Color value  |


# Abstraction

You are **abstract** when you talk able the similarities between two different things. You are **concrete** when you talk about the differences. In English class, you might be asked to "Compare and Contrast Melville to Dickens". This means make a list the similarities betweent the two authors, and a list of differences. If I say, "Talk about an umbrella and a pencil". If you immediately say the two are different, you are concrete. If you say, "They both have weight, are created by humans, are useful tools, etc." then you are abstract. 

"You can't compare apples to oranges!". Well, yes you can. They are both fruit.

# Type

A **type** is a set of all possible values for a variable. It can be an infinite set, or a rule on what are allowed values. Example:

* Natural number: 1, 2, 3, 4, ...
* Even number
* Odd number
* Prime number
* Whole number: 0, 1, 2, 3, 4, ...
* Integer: positive and negative whole numbers: ..., -3, -2, -1, 0, 1, 2, 3, ...
* Boolean: {FALSE, TRUE} or (0, 1) or {No, Yes} etc.
* Floats
* Dates
* Times
* DateTimes
* Strings

You can create your own "custom" types too, like "All strings over the uppercase alphabet that begin with the letter 'Q' and are five letters long"

# Property

A **property** is a named variable that has a type. 

# Value

A **value** specific choice of a type. For example "3" is a value of the Natural Numbers type. Since properties have a type, we can also talk able the value of a property.

# Class

A **class** is a set of named properties that have a default value, like "" for strings or 0 for numbers. Example: a "Person" object might have a "Firstname" and a "Lastname" property.
An "Employee" class might inherit from a "Person" class. For example, an "Employee" object might have a "Title" property, e.g. a value of "President".
This means that if you create an instance of the Employee object, you have three properties: Firstname, Lastname, and Title.

# Object

An **object** is an instance of a class. This means that all objects are created from some type of class. For example, Person1 is a person with Firstname = "Fred" and "Lastname" = "Flintstone".

A object contains these concepts and behaviors:

* It has **identity**, which means you can distinguish one object from another and say that they are different. You can also determine if they are the same. For example, in math we have the object "SEVEN" and the object "7" but we say they are the same object, with two different names. If I show you two different pictures of the Statue of Liberty, you say they represent the same object. If instead we talk about the physical pictures, you say they are different picture objects, that represent the same object. If I show you a picture of the Eiffel Tower, you say it is a different object than the Statue of Liberty. If someone walks in the room, you say "That's Fred". If Fred walks out of the room and then back in the room, you say "That's Fred" - the same person object, just at different times.
* It might have an **identifier**, which is just a name for the object. This is true in database systems. If you have a set of people (i.e. a table or list of records) then you want to have exactly one identifier per object. If you have two records for the same object, we say you have a **duplicate** in your system. An identifier has these characteristics:

    * **Immutable** - When the record is created for an object, its identifier never changes over the lifetime of the record.
    * **Uniqueness** - No two different objects can have the same identifier. 

# Data Science

We organize our data into a database so we can access it quickly for our data science experiments. The database is a set of classes called tables or datasets.

* Each class is a set of objects; e.g. "People", "Places", "Pets", etc.
* Each object is a row in the table.
* Each property is a column.
* Each value is a cell.

A database of tables might have these tables:

## People

| id  | Firstname | Lastname   | Age |
| --- | --------- | ---------- | --- |
| 1   | Fred      | Flintstone | 36  |
| 2   | Wilma     | Flintstone | 34  |
| 3   | Barney    | Rubble     | 35  |
| 4   | Betty     | Rubble     | 33  |
| 5   | BamBam    | Flintstone | 5   |
| 6   | Pebbles   | Rubble     | 4   |
| 7   | George    | Jetson     | 35  |

## Employees

| id  | Title                  | CompanyId |
| --- | ---------------------- | --------- |
| 1   | Bronto-Crane Operator  | 1         |
| 3   | Bronto-Crane Operator  | 1         |
| 7   | Digital Index Operator | 2         |

## Companies
| id  | Name                      |
| --- | ------------------------- |
| 1   | Bedrock Quarry and Gravel |
| 2   | Spacely Space Sprockets   |


## Relations

| From | To  | Relationship |
| ---- | --- | ------------ |
| 1    | 2   | Husband      |
| 2    | 1   | Wife         |
| 3    | 4   | Husband      |
| 4    | 3   | Wife         |
| 1    | 5   | Parent       |
| 2    | 5   | Parent       |
| 5    | 1   | Child        |
| 5    | 2   | Child        |
| 3    | 6   | Parent       |
| 4    | 6   | Parent       |
| 6    | 3   | Child        |
| 6    | 4   | Child        |

This table shows (for example) that the Pebbles is the child of both Barney and Betty.
When the id of one table is used in another table, we say the two tables are related.

## Diagramming

![](/static/images/20251116151745.png)

In the diagram above:

* Open arrows represent ISA relationships. An Employee is a Person. These are implemented as primary key to primary key relations.
* Closed arrows represent HASA relationships. An employee has a company.

RULE: You should never have cycles in your relationships; e.g. A points to B, and B points to A. These are called **many-to-many** relations but it is bad architecture design. Rather you should create a third table (called a bridge or crosswalk table) that relates A to B. Then C points to A and B instead. The **Relations** table is just that - a table that creates a many-to-many relation between people and people. A person can have multiple parents, and a parent can have multiple children.

All databases give you the ability to select all rows from a table, join rows from different tables, filter the rows that are returned, print out the column names and values of the rows returned, add a new row, delete a row, update the value of a row/column.








