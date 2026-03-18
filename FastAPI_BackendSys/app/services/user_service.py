from app.models.user_model import User

def create_user(db, user):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db):
    return db.query(User).all()

def update_user(db, user_id, user):
    existing = db.query(User).filter(User.id == user_id).first()
    
    if not existing:
        return None

    existing.name = user.name
    existing.email = user.email
    existing.age = user.age

    db.commit()
    db.refresh(existing)
    return existing

# ✅ ADD THIS
def delete_user(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"error": "User not found"}
    
    db.delete(user)
    db.commit()
    
    return {"message": "User deleted successfully"}