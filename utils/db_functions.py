from utils.db import execute, fetch


async def db_check_token_user(user):
    query = """select * from users where username = :username"""
    values = {"username": user.username}
    result = await fetch(query, False, values)
    if result is None:
        return None
    else:
        return result


async def db_check_jwt_username(username):
    query = """select * from users where username = :username"""
    values = {"username": username}

    result = await fetch(query, True, values)
    if result is None:
        return False
    else:
        return True


async def db_insert_user(user):
    query = """insert into users(firstname, lastname, username, password, email)
                values(:firstname,:lastname,:username,:password,:email)"""
    values = dict(user)

    await execute(query, False, values)


async def db_check_user(email):
    query = """select firstname, lastname, username, email from users where email = :email"""
    values = {"email": email}
    user = await fetch(query, True, values)
    if user is None:
        return False
    else:
        return user


async def db_insert_item(item):
    query = """insert into items(name, quantity, price, description, owner)
                values(:name, :quantity, :price, :description, :owner)"""
    values = dict(item)

    await execute(query, False, values)


async def db_get_all_item():
    query = """select name, quantity, price, description, owner  from items"""
    values = dict()
    result = await fetch(query, False, values)
    return result


async def db_get_user_items(owner):
    query = (
        """select name, quantity, price, description from items where owner = :owner"""
    )
    values = {"owner": owner}
    result = await fetch(query, False, values)
    return result


async def db_get_item_with_id(id):
    query = (
        """select name, quantity, price, description, owner from items where id = :id"""
    )
    values = {"id": id}
    item = await fetch(query, True, values)
    return item


async def db_update_item(id, name, quantity, price, description):
    query = """update items set name =:name, quantity =:quantity, price =:price, 
                                    description =:description where id=:id"""
    values = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "description": description,
        "id": id,
    }
    await execute(query, False, values)


async def db_delete_item_with_id(id):
    query = """delete from items where id =:id"""
    values = {"id": id}
    await execute(query, False, values)
