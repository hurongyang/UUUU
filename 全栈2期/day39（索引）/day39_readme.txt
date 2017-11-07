事务：innodb--------------------------------------------------------------------------
    p12(out status int):
        try:
            insert into tb1()
            update tb2...
            set status=1
        except ...:
            set status=0
    call p12()

索引----------------------------------------------------------------------------------
    功能：
        - 约束
            - 主键
            - 外键
            - 唯一
            - 普通
            - 组合
        - 加速查找
        
    为什么索引可以这么快？
    name列建立索引===========>创建一个文件，name列所有数据拿出来
    name='eric' > 6 # 4
    name='tony' > 66 # 3
    1024
                           30
 
                10                        40
         
           5         15            35             66 （真是表中我当前行的数据在硬盘上的位置）
         
        1    6     11    19      21      39     55     100
                 
        1    6     11    19      21      39     55     100         
        1    6     11    19      21      39     55     100         
        1    6     11    19      21      39     55     100         
        1    6     11    19      21      39     55     100         
        1    6     11    19      21      39     55     100
    B-tree
        name索引
    
    都有那些索引：
    1、创建表
        nid name pwd email
        数据文件：硬盘，。。。。。。。
        
    2、创建索引
        nid主键索引：
        name列创建索引
            - 数据name列数据全部拿到
            - name每一个转化成一个数字,算法
            - 
        
                               30
     
                    10                        40
             
               5         15            35             66（位置,位置,位置） （数据表中我当前行的数据在硬盘上的位置）
             
            1    6     11    19      21      39     55     100
            
            - 索引文件： 硬盘
        pwd列创建索引
            - 数据pwd列数据全部拿到
            - pwd每一个转化成一个数字
            - 
                               30
     
                    10                        40
             
               5         15            35             66 （数据表中我当前行的数据在硬盘上的位置）
             
            1    6     11    19      21      39     55     100
            - 索引文件： 硬盘
        
        
    搜索：
        select * from tb1 where name='alex'
        'alex'转换成数字
        select * from tb1 where email='alex'

    索引种类：
        普通索引 - 加速查找，可以重复
        唯一索引 - 加速查找，约束列数据不能重复,可以为null
        主键索引 - 加速查找，约束列数据不能重复,不能null
        组合索引 - 多列可以创建一个索引文件
            - 普通组合索引
            - 联合唯一索引

    1、普通索引
        create index 索引名称 on  表（列名）
    
    2、唯一索引
        create unique index

    3、主键索引
        - 不能重复，不能null
        
    4、组合索引
        name,pwd
        - 普通组合索引：
                无约束
                name,pwd
        - 联合唯一索引：
                有约束，两列数据同时不相同，才能插入，不然报错
                name,pwd
                
        查找：最左匹配
        select * from tb1 where name = 'alex'
        select * from tb1 where name = 'alex' and pwd='123'
        select * from tb1 where pwd='123'  # 不会走索引
        
        查找：最左匹配
        name,pwd,email 
        select * xx where name ='alex'
        select * xx where pwd ='alex'
        select * xx where email ='alex'
        select * xx where name='alex' and pwd='xx'
        
    
    ================================================================================================
    1、覆盖索引--------------------------------------------------------------------------------------
        
        select * from tb where nid=1
        # 先去索引中找，
        # 在去数据表找
        
        select nid from tb where nid < 10 
        # 先去索引中找
            
        -- 情况应用上索引，并且不用去数据表中操作，覆盖索引0
        -- 只需要在索引表中就能获取到数据时，
    2、合并索引-------------------------------------------------------------------------------------
        nid   name(单独索引)    email（单独索引）    pwd
        
        select * from tb where name='alex'
        select * from tb where email='alex3714@163.com'
        
        select * from tb where name='alex' or email='alex3714@163.com'

        nid   name(组)    email（合）    pwd
        # 最左前缀
        
        select * from tb where name='alex'
        select * from tb where email='alex3714@163.com' ########无法满足########
        
        select * from tb where name='alex' or email='alex3714@163.com'
        
       用户表：
            nid   username（组）    password（合）
             1     alex         123
             2     shaogbing    123
             
            select * from tb where username='xx' and password='xx'
            select * from tb where username='xx'
            # select * from tb where password='xx'
            
            --> 组合和合并索引取舍？业务需求来决定

    3、执行计划 - 相对比较准确表达出当前SQL运行状况(explain SQL语句)--------------------------------
        是否走索引，不走索引

        1、explain SQL语句
            type： ALL    - 全数据表扫描
            type： index  - 全索引表扫面
            
        2、limit 
            select * from tb1 where email='123'                 全表扫描
            select * from tb1 where email='123' limit 1;        limit1只会扫第一行，不会全表扫
        -----SQL： ALL、Index，都是有优化的余地 -------
        
    4、如何命中索引---------------------------------------------------------------------------------
        nid name          ctime
                     2016-9-10 11:59

        当前时间：

                     2016/9/10
        select * from tb1 where conv(ctime,'.,..') = time;（子查询使用函数，即使ctime是索引也不会走索引）
        # 转换
        select * from tb1 where ctime = 转(2016/9/10)=> 2016-9-10 (把查询时间转换成数据库存储的时间格式，命中索引)
    
    5、分页-----------------------------------------------------------------------------------------
        limit x,m :  表x+m

        where nid>10000 直接跳过 钱10000条数，继续往下扫

        每页：10条
        1     2    3     4  ...    18  19  20  21
        1     17   31   45
        16    29   42   90  
            
        -- nid排列可能中断的
        
        ---------- 方式： 上一页下一页 ----------
        
        1、当用查看页面时，第一页 limit 0,10： nid: 1 - 16
        
        
        2、第一页 limit 10,10： nid: 17 - 36
        3、第一页 limit 100000,10： nid: 17 - 36

        
        2、第一页 where nid>16 limit 10： nid: 17 - 36
        3、第一页 where nid>36 limit 10： nid: 170 - 360
    6、慢SQL日志-------------------------------------------------------------------------------------

    
    
    
    
    
    
    
    
    
    
    
    
    
    
        















