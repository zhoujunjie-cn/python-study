def calc_order_cost(*args, coupon, score, express):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2. 扣减优惠券：满5000可用，优惠券金额不超过商品总价
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3. 扣减积分抵扣：满5000可用，100积分抵1元，抵扣额不超过当前总价
    deduct_score = score // 100
    if total_cost >= 5000 and deduct_score <= total_cost:
        total_cost -= deduct_score

    # 4. 增加运费
    total_cost += express

    return total_cost
total=calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=40000,express=9.9)
print(total)