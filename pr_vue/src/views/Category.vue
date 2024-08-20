<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-3 has-text-centered">{{ category.name }}</h2>
                <!-- <div class="section pt-4 pb-1">
                    <div class="dirbread">
                        <nav class="breadcrumb" aria-label="breadcrumbs">
                            <ul class="container is-size-6">
                                <li class="has-text-grey"><a href="/">ممنتو</a></li>
                                <li class="is-active"><a v-bind:href="category.get_absolute_url"
                                        aria-current="page">{{ category.name }}</a></li>
                            </ul>
                        </nav>
                    </div>
                </div> -->
                <BreadcrumbBox />
            </div>

            <ProductBox v-for="product in category.products" v-bind:key="product.id" v-bind:product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ProductBox from '@/components/ProductBox'
import BreadcrumbBox from '@/components/BreadcrumbBox'

export default {
    name: 'Category',
    components: {
        ProductBox,
        BreadcrumbBox
    },
    data() {
        return {
            category: {
                products: [],
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
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
                    console.log(this.category)
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
        }
    }
}
</script>

<!-- <style lang="scss">
.dirbread {
    direction: rtl;
}
</style> -->