#
#Run the create_ins_trigger script after this
#Create the master record 
CREATE TABLE set_top.vuetrakmstr (
    set_top_id      int not null,
    view_title      varchar(100),
    logdate         date not null,
    revenue         real
	);

#2014 data tables
CREATE TABLE set_top.vuer_data_y2014m01 (CHECK ( logdate >= DATE '2014-01-01' AND logdate < DATE '2014-02-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m01_logdate ON set_top.vuer_data_y2014m01 (logdate);

CREATE TABLE set_top.vuer_data_y2014m02 (CHECK ( logdate >= DATE '2014-02-01' AND logdate < DATE '2014-03-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m02_logdate ON set_top.vuer_data_y2014m02 (logdate);

CREATE TABLE set_top.vuer_data_y2014m03 (CHECK ( logdate >= DATE '2014-03-01' AND logdate < DATE '2014-04-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m03_logdate ON set_top.vuer_data_y2014m03 (logdate);

CREATE TABLE set_top.vuer_data_y2014m04 (CHECK ( logdate >= DATE '2014-04-01' AND logdate < DATE '2014-05-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m04_logdate ON set_top.vuer_data_y2014m04 (logdate);

CREATE TABLE set_top.vuer_data_y2014m05 (CHECK ( logdate >= DATE '2014-05-01' AND logdate < DATE '2014-06-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m05_logdate ON set_top.vuer_data_y2014m05 (logdate);

CREATE TABLE set_top.vuer_data_y2014m06 (CHECK ( logdate >= DATE '2014-06-01' AND logdate < DATE '2014-07-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m06_logdate ON set_top.vuer_data_y2014m06 (logdate);

CREATE TABLE set_top.vuer_data_y2014m07 (CHECK ( logdate >= DATE '2014-07-01' AND logdate < DATE '2014-08-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m07_logdate ON set_top.vuer_data_y2014m07 (logdate);

CREATE TABLE set_top.vuer_data_y2014m08 (CHECK ( logdate >= DATE '2014-08-01' AND logdate < DATE '2014-09-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m08_logdate ON set_top.vuer_data_y2014m08 (logdate);

CREATE TABLE set_top.vuer_data_y2014m09 (CHECK ( logdate >= DATE '2014-09-01' AND logdate < DATE '2014-10-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m09_logdate ON set_top.vuer_data_y2014m09 (logdate);

CREATE TABLE set_top.vuer_data_y2014m10 (CHECK ( logdate >= DATE '2014-10-01' AND logdate < DATE '2014-11-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m10_logdate ON set_top.vuer_data_y2014m10 (logdate);

CREATE TABLE set_top.vuer_data_y2014m11 (CHECK ( logdate >= DATE '2014-11-01' AND logdate < DATE '2014-12-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m11_logdate ON set_top.vuer_data_y2014m11 (logdate);

CREATE TABLE set_top.vuer_data_y2014m12 (CHECK ( logdate >= DATE '2014-12-01' AND logdate < DATE '2015-01-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2014m12_logdate ON set_top.vuer_data_y2014m12 (logdate);

#2015 partitions
CREATE TABLE set_top.vuer_data_y2015m01 (CHECK ( logdate >= DATE '2015-01-01' AND logdate < DATE '2015-02-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m01_logdate ON set_top.vuer_data_y2015m01 (logdate);

CREATE TABLE set_top.vuer_data_y2015m02 (CHECK ( logdate >= DATE '2015-02-01' AND logdate < DATE '2015-03-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m02_logdate ON set_top.vuer_data_y2015m02 (logdate);

CREATE TABLE set_top.vuer_data_y2015m03 (CHECK ( logdate >= DATE '2015-03-01' AND logdate < DATE '2015-04-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m03_logdate ON set_top.vuer_data_y2015m03 (logdate);

CREATE TABLE set_top.vuer_data_y2015m04 (CHECK ( logdate >= DATE '2015-04-01' AND logdate < DATE '2015-05-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m04_logdate ON set_top.vuer_data_y2015m04 (logdate);

CREATE TABLE set_top.vuer_data_y2015m05 (CHECK ( logdate >= DATE '2015-05-01' AND logdate < DATE '2015-06-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m05_logdate ON set_top.vuer_data_y2015m05 (logdate);

CREATE TABLE set_top.vuer_data_y2015m06 (CHECK ( logdate >= DATE '2015-06-01' AND logdate < DATE '2015-07-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m06_logdate ON set_top.vuer_data_y2015m06 (logdate);

CREATE TABLE set_top.vuer_data_y2015m07 (CHECK ( logdate >= DATE '2015-07-01' AND logdate < DATE '2015-08-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m07_logdate ON set_top.vuer_data_y2015m07 (logdate);

CREATE TABLE set_top.vuer_data_y2015m08 (CHECK ( logdate >= DATE '2015-08-01' AND logdate < DATE '2015-09-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m08_logdate ON set_top.vuer_data_y2015m08 (logdate);

CREATE TABLE set_top.vuer_data_y2015m09 (CHECK ( logdate >= DATE '2015-09-01' AND logdate < DATE '2015-10-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m09_logdate ON set_top.vuer_data_y2015m09 (logdate);

CREATE TABLE set_top.vuer_data_y2015m10 (CHECK ( logdate >= DATE '2015-10-01' AND logdate < DATE '2015-11-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m10_logdate ON set_top.vuer_data_y2015m10 (logdate);

CREATE TABLE set_top.vuer_data_y2015m11 (CHECK ( logdate >= DATE '2015-11-01' AND logdate < DATE '2015-12-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m11_logdate ON set_top.vuer_data_y2015m11 (logdate);

CREATE TABLE set_top.vuer_data_y2015m12 (CHECK ( logdate >= DATE '2015-12-01' AND logdate < DATE '2016-01-01' ) ) INHERITS (set_top.vuetrakmstr) ;
CREATE INDEX vuer_data_y2015m12_logdate ON set_top.vuer_data_y2015m12 (logdate);