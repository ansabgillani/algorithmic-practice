def suggestedProducts(products, searchWord):
    products.sort()
    result = []
    prefix = ""
    for char in searchWord:
        prefix += char
        matches = [product for product in products if product.startswith(prefix)][:3]
        result.append(matches)
    return result

# Test cases
print(suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))  # [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
print(suggestedProducts(["havana"], "havana"))  # [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]