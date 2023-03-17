from web_app import db

def get_garages_list():
    sql = f"""
    select * from sc_info.garage_list;
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info

def get_garage_info(garage_id):
    sql = f"""
    select * from sc_info.garage_list where garage_id = {garage_id} ;
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info

def get_services_list():
    sql = f"""
      select * from sc_info.service_list;
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info

def get_subscription_packages():
    sql = f"""
      select * from sc_info.sub_package;
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info
  
def get_search_list(search_str):
    sql = f"""
      Select * from sc_info.garage_list where (
      garage_name like ('%{search_str}%') or 
      sc_loc like ('%{search_str}%')
      )
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info
  
def get_user_sub(user_id):
    sql = f"""
      select sp.package_price ,gl.garage_name,sp.package_name  from sc_info.subscription_list sl inner join sc_info.sub_package sp on 
 sp.sub_pack_id = sl.package_id inner join sc_info.garage_list gl on sl.garage_id = gl.garage_id  where user_id = {user_id};
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info
  
def get_user_bookings(user_id):
    sql = f"""
        select b.book_id,b.rec_date,b.service_ids,b.timing,b.delivery,b.user_loc, b.brand,b.brand_model,gl.garage_name,gl.image  from sc_info.bookings b INNER JOIN sc_info.garage_list gl ON gl.garage_id = b.garage_id where b.user_id = {user_id};
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info
  
  
def get_user_services(service_ids):
    sql = f"""
        select service_name from sc_info.service_list where service_id in ({service_ids}); 
    """
    user_info = db.session.execute(sql).fetchall()
    return user_info
