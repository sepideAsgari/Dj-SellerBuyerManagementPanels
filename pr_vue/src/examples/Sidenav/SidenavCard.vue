<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
const store = useStore();

const isRTL = computed(() => store.state.isRTL);
const layout = computed(() => store.state.layout);
defineProps({
  card: {
    type: Object,
    required: true,
    title: String,
    description: String,
    links: {
      type: Array,
      label: String,
      route: String,
      color: String,
    },
  },
});
</script>
<template>
  <div v-show="layout !== 'landing'" class="card card-plain shadow-none" id="sidenavCard">
    <div class="p-3 card-body text-center w-100 pt-0">
      <img class="w-50 mx-auto" src="@/assets/img/illustrations/icon-documentation.svg" alt="sidebar_illustration" />

      <h6 v-if="isRTL" class="mb-0 text-dark up">لورم</h6>

      <h6 v-else class="mb-0 text-dark up">Need Help ?</h6>

      <p v-if="isRTL" class="text-xs font-weight-bold">
        لورم
      </p>
      <p v-else class="text-xs font-weight-bold">Please check our docs</p>
    </div>

    <a v-if="isRTL" href="https://www.creative-tim.com/learning-lab/vue/overview/argon-dashboard/" target="_blank"
      class="mb-3 btn btn-dark btn-sm w-100">
      دکمه ۱
    </a>

    <a v-else href="#" target="_blank" class="mb-3 btn btn-dark btn-sm w-100">
      Documentation
    </a>

    <a v-if="isRTL" href="#" target="_blank" class="mb-3 btn btn-success btn-sm w-100">دکمه ۲
    </a>

    <a v-else href="#" target="_blank"
      class="mb-3 btn btn-success btn-sm w-100">
      Upgrade to pro
    </a>
  </div>
</template>
