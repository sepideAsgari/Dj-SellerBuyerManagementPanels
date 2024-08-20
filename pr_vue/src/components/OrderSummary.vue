<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

        <h4 class="is-size-5 this-is-rtl">شرح محصولات</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>مجموع</th>
                    <th>تعداد</th>
                    <th>قیمت</th>
                    <th>شرح محصول</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="item in order.items" v-bind:key="item.product.id">
                    <td>{{ getItemTotal(item).toLocaleString() }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ getItemPrice(item).toLocaleString() }}</td>
                    <td>{{ item.product.name }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        getItemPrice(item) {
            return 1 * item.product.price
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
    }
}
</script>