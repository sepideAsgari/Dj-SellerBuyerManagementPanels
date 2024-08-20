<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
import AuthorsTable from "./components/AuthorsTable.vue";
import ProjectsTable from "./components/ProjectsTable.vue";
import { onMounted, onBeforeUnmount } from "vue";
const store = useStore();
const hideFooter = () => {
  store.commit('hideFooter', false);
};

const showFooterAgain = () => {
  store.commit('showFooter', true);
};

onMounted(() => {
  hideFooter();
});

onBeforeUnmount(() => {
  showFooterAgain();
});
</script>
<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-12">
        <authors-table />
      </div>
    </div>
    <div class="mt-4 row">
      <div class="col-12">
        <projects-table />
      </div>
    </div>
  </div>
</template>
