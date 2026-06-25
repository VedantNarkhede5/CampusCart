from difflib import SequenceMatcher
from .models import Product
import random


def similarity(a, b):

    return SequenceMatcher(
        None,
        str(a).lower(),
        str(b).lower()
    ).ratio()


def get_home_recommendations(user):

    products = list(
        Product.objects.filter(
            is_sold=False
        ).exclude(
            seller=user
        )
    )

    if len(products) <= 3:
        return products

    scored_products = []

    for product in products:

        score = 0

        # 1. Category Weight (Highest Priority)

        same_category_count = Product.objects.filter(
            category=product.category,
            is_sold=False
        ).exclude(
            seller=user
        ).count()

        score += same_category_count * 20

        # 2. Title Similarity

        title_score = 0

        for other in products:

            if product.id != other.id:

                title_score += similarity(
                    product.title,
                    other.title
                )

        score += title_score * 15

        # 3. Description Similarity

        description_score = 0

        for other in products:

            if product.id != other.id:

                description_score += similarity(
                    product.description,
                    other.description
                )

        score += description_score * 10

        # 4. Price Similarity Bonus

        for other in products:

            if product.id != other.id:

                difference = abs(
                    float(product.price) -
                    float(other.price)
                )

                if difference <= 100:

                    score += 10

                elif difference <= 300:

                    score += 5

        # 5. Condition Bonus

        if product.condition == "New":

            score += 15

        elif product.condition == "Good":

            score += 8

        # 6. Urgent Listings

        if product.is_urgent:

            score += 25

        # 7. Fresh Listings Bonus

        score += random.uniform(1, 5)

        scored_products.append(
            (score, product)
        )

    scored_products.sort(
        key=lambda x: x[0],
        reverse=True
    )

    recommendations = []

    used_categories = set()

    for score, product in scored_products:

        if product.category not in used_categories:

            recommendations.append(product)

            used_categories.add(
                product.category
            )

        if len(recommendations) == 3:
            break

    # Fallback

    if len(recommendations) < 3:

        for score, product in scored_products:

            if product not in recommendations:

                recommendations.append(product)

            if len(recommendations) == 3:
                break

    return recommendations
