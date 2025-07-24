from flask import Blueprint, jsonify, request
from src.app.models.product import Product
from src.app.models.category import Category
from src.app.schemas.product import ProductSchema
from src.app.config import Config

api_bp = Blueprint("api", __name__)


@api_bp.route(Config.INFO_ROUTE, methods=["GET"])
def info():
    name_filter = request.args.get("name")
    on_main_filter = request.args.get("on_main")
    category_filter = request.args.get("category")

    query = Product.query

    if name_filter:
        query = query.filter(Product.name.ilike(f"%{name_filter}%"))
    elif on_main_filter is not None:
        if on_main_filter.lower() in ("true", "1", "yes"):
            query = query.filter(Product.on_main.is_(True))
        elif on_main_filter.lower() in ("false", "0", "no"):
            query = query.filter(Product.on_main.is_(False))
    elif category_filter:
        query = query.filter(
            Product.category.has(Category.name.ilike(f"%{category_filter}%"))
        )

    products = query.all()
    categories = Category.query.all()

    product_schemas = [
        ProductSchema(
            id=p.id,
            name=p.name,
            price=p.price,
            image_url=p.image_url,
            on_main=p.on_main,
            category=p.category.name if p.category else None,
        ).model_dump()
        for p in products
    ]

    return jsonify(
        {
            "total_products": len(products),
            "categories": [c.name for c in categories],
            "products": product_schemas,
        }
    )
