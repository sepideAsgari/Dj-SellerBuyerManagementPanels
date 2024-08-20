<template>
    <tr>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
        <td>
            <rb>ت </rb>{{ getItemTotal(item).toLocaleString() }}
        </td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)">-</a>
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <!-- <td>{{ item.product.price }} ت</td> -->
        <td>
            <rb>ت </rb>{{ getItemPrice(item).toLocaleString() }}
        </td>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        getItemPrice(item) {
            return item.product.price * 1
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    },
}
</script>
<style lang="scss">
// .table th:not([align]) {
//     text-align: var(--bulma-table-cell-text-align);
//     text-align: center;
// }
// .table tbody tr:last-child td, .table tbody tr:last-child th {
//   border-bottom-width: 0;
//   text-align: center;
// }
.table thead td,
.table thead th {
    text-align: center !important;
}

.table tbody tr:last-child td,
.table tbody tr:last-child th {
    text-align: center !important;
}

table td:not([align]),
table th:not([align]) {
    text-align: center !important;
}
</style>