<template>
    <div class="section pt-4 pb-1 pl-0 pr-0">
        <div class="dirbread">
            <nav class="breadcrumb" aria-label="breadcrumbs">
                <ul class=".container.is-max-widescreen mb-0 is-size-6 is-size-7-mobile">
                    <!-- <ul class="container is-size-7-mobile"> -->
                    <li class="has-text-link"><a href="/">ممنتو</a></li>
                    <li class="has-text-link"><a v-bind:href="category.get_absolute_url" aria-current="page">{{
                            category.name }}</a></li>
                    <li class="has-text-primary"><a v-bind:href="product.get_absolute_url" aria-current="page">{{ product.name
                            }}</a></li>
                </ul>
            </nav>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Breadcrumbv2Box',
    props: {
        category: Object

    },
    data() {
        return {
            category: {
                products: [],
            },
            product: {
                product: []
            }
        }
    },
    mounted() {
        this.getCategory()
        this.getProduct()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
            if (to.name === 'Product') {
                this.getProduct()
            }

        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | صنایع دستی'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        },
        async getProduct() {
            const categorySlug = this.$route.params.category_slug
            const productSlug = this.$route.params.product_slug

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/products/${categorySlug}/${[productSlug]}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | صنایع دستی'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
<style lang="scss">
.dirbread {
    direction: rtl;
}

.breadcrumb a {
    padding-left: 1px;
    padding-right: 1px;
}

</style>