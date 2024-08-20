<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">سبد خرید من</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th></th>
                            <th>مجموع</th>
                            <th>تعداد</th>
                            <th>قیمت</th>
                            <th>شرح محصول</th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem v-for="item in cart.items" v-bind:key="item.product.id" v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                    </tbody>
                </table>

                <p v-else>
                    سبد خرید شما خالی است!
                </p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">شرح محصولات منتخب من</h2>
                <p>مجموع قیمت کالاها :
                    <strong>{{ cartTotalPrice.toLocaleString() }}</strong>
                </p>
                <p>مجموع تعداد کالاها :
                    <strong>{{ cartTotalLength }}</strong>
                </p>
                <hr>

                <a class="button is-success" @click="proceedToCheckout">پرداخت و ارسال</a>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
import { toast } from 'bulma-toast'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        },
        proceedToCheckout() {
            if (this.cartTotalLength === 0) {
                toast({
                    message: 'سبد خرید شما خالی است. لطفاً از <a href="/" class="has-text-link">فروشگاه</a> محصولاتی را به سبد خرید اضافه کنید.',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 4000,
                    position: 'bottom-right'
                })
            } else {
                this.$router.push('/cart/checkout')
            }
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>
