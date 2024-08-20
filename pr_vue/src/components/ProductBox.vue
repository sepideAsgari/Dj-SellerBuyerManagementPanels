<template>
    <div class="column is-3">
        <div class="card w-96 bg-base-100 shadow-xl">
            <figure><img v-bind:src="product.get_make_product_image" alt="Shoes" /></figure>
            <div class="card-body">
                <h3 class="card-title is-size-6">
                    {{ product.name }}
                </h3>
                <span class="tag is-warning">جدید</span>
                <p>{{ product.price }}</p>
                <div class="card-actions justify-center">
                    <span class="tag is-warning is-light">{{ product.get_category_name }}</span>
                    <div class="tag is-success is-light">
                        <router-link v-bind:to="product.get_absolute_url">نمایش</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object,
    },
}
</script>

<style lang="scss" scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}

.card-title {
    direction: rtl;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
