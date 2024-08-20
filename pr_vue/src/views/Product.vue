<template>
    <div class="section pt-2">
        <div class="page-product">
            <Breadcrumbv2Box />
            <div class="columns is-multiline reverse-columns">
                <div class="column is-7"> <!-- ستون اطلاعات محصول -->
                    <div class="section">
                        <h3 class="title is-size-5-mobile">{{ product.name }}</h3>
                        <!-- <h3 class="subtitle is-size-5-mobile">{{ product.averageReview }}</h3>
                        <h3 class="subtitle is-size-5-mobile">{{ product.countReview }}</h3> -->
                        <h5 class="subtitle is-size-5-mobile">امتیاز محصول {{ product.averageReview }} از {{ product.countReview }} دیدگاه</h5>
                    </div>
                    <p class="pprice"><strong>قیمت: </strong>تومان{{ product.price }}</p>

                    <div class="field has-addons mt-6">
                        <div class="control">
                            <input type="number" class="input" min="1" v-model="quantity">
                        </div>

                        <div class="control">
                            <a class="button is-success" @click="addToCart()">افزودن به سبد</a>
                        </div>
                    </div>
                </div>

                <div class="column is-5"> <!-- ستون تصویر -->
                    <figure class="image mb-6">
                        <img v-bind:src="product.get_image" class="product-image">
                    </figure>
                </div>
            </div>
            <div class="column">
                <p class="pdescription">{{ product.description }}</p>
            </div>
        </div>
    </div>
</template>




<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import Breadcrumbv2Box from '@/components/Breadcrumbv2Box'
// import Ratestars from '@/components/Ratestars.vue';

export default {
    name: 'Product',
    components: {
        Breadcrumbv2Box,
        // Ratestars
    },
    data() {
        return {
            // products: [],
            product: {},
            quantity: 1
        }
    },
    mounted() {
        //     axios.get('/api/v1/products/average-ratings/')
        //   .then(response => {
        //     this.products = response.data;
        //   })
        //   .catch(error => {
        //     console.error('Error fetching product average ratings:', error);
        //   });
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | ' + 'صنایع دستی'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
            toast({
                message: '.' + ' محصول ' + this.product.name + ' به سبد خرید افزوده شد ',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'bottom-right',
            })
        }
    }
}
</script>
<!-- <style lang="scss">
@media(max-width: 767px) {
    .reverse-columns {
        flex-direction: column-reverse;
        display: flex;
    }
}

.title {
    direction: rtl !important;
}

.pdescription {
    direction: rtl !important;
}

.pprice {
    direction: rtl !important;
}

.notification>.delete {
    position: absolute;
    inset-inline-end: 0.5rem;
    top: 0.5rem;
}
</style> -->
<style lang="scss">
@media (min-width: 768px) {
    .column.is-8 {
        flex: 0 0 70%;
        max-width: 70%;
    }

    .column.is-4 {
        flex: 0 0 30%;
        max-width: 30%;
    }
}

.product-image {
    // max-width: 600px;
    width: 100%;
    height: auto;
}

.title {
    direction: rtl !important;
}

.pdescription {
    direction: rtl !important;
}

.pprice {
    direction: rtl !important;
}

.notification>.delete {
    position: absolute;
    inset-inline-end: 0.5rem;
    top: 0.5rem;
}

@media (max-width: 767px) {
    .reverse-columns {
        display: flex;
        flex-direction: column-reverse;
    }
}
</style>
