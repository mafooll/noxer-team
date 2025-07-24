from src.app.extensions import db
from src.app.models.product import Product
from src.app.models.category import Category
from loguru import logger


def sync_data(products):
    try:
        categories_dict = {c.name: c for c in Category.query.all()}
        created_count = 0
        updated_count = 0
        skipped_count = 0

        for item in products:
            product_id = item.get("Product_ID")
            name = item.get("Product_Name")

            if not product_id or not name:
                logger.warning(f"Пропущен товар без ID или имени: {item}")
                continue

            price = None
            if item.get("parameters"):
                price = item["parameters"][0].get("price")

            image_url = None
            if item.get("images"):
                image_url = item["images"][0].get("Image_URL")

            on_main = item.get("OnMain", False)

            category_name = None
            if item.get("categories"):
                category_name = item["categories"][0].get("Category_Name")

            category = None
            if category_name:
                if category_name not in categories_dict:
                    category = Category(name=category_name)
                    db.session.add(category)
                    db.session.flush()
                    categories_dict[category_name] = category
                else:
                    category = categories_dict[category_name]

            category_id = category.id if category else None

            product = Product.query.get(product_id)
            if product:
                if (
                    product.name != name
                    or product.price != price
                    or product.image_url != image_url
                    or product.on_main != on_main
                    or product.category_id != category_id
                ):
                    product.name = name
                    product.price = price
                    product.image_url = image_url
                    product.on_main = on_main
                    product.category_id = category_id
                    updated_count += 1
                else:
                    skipped_count += 1
            else:
                new_product = Product(
                    id=product_id,
                    name=name,
                    price=price,
                    image_url=image_url,
                    on_main=on_main,
                    category_id=category_id,
                )
                db.session.add(new_product)
                created_count += 1

        db.session.commit()
        logger.info(
            f"Синхронизация завершена. Создано: {created_count}"
            f" обновлено: {updated_count}, без изменений: {skipped_count}"
        )
    except Exception as e:
        db.session.rollback()
        logger.exception(f"Ошибка при синхронизации с БД: {e}")
