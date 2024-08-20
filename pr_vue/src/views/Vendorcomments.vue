<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
import Sidenav from "@/examples/Sidenav"
import MasterCard from "@/examples/Cards/MasterCard.vue";
import DefaultInfoCard from "@/examples/Cards/DefaultInfoCard.vue";
import PaymentCard from "./components/PaymentCard.vue";
import InvoiceCard from "./components/InvoiceCard.vue";
import BillingCard from "./components/BillingCard.vue";
import TransactionCard from "./components/TransactionCard.vue";

import { onMounted, onBeforeUnmount } from "vue";
const store = useStore();
const showSidenav = computed(() => store.state.showSidenav);
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
  <div class="g-sidenav-hidden">
    <sidenav v-if="showSidenav" />
    <main class="main-content position-relative max-height-vh-100 h-100 border-radius-lg" style="@media (min-width: 1200px) {
  .sidenav.fixed-end + .main-content {
    margin-right: 7.125rem;
  }
}">
      <div class=" container-fluid">
        <div class="row">
          <div class="col-lg-8">
            <div class="row mt-4">
              <div class="col-xl-6 mb-xl-0 mb-4">
                <master-card />
              </div>
              <div class="col-xl-6">
                <div class="row">
                  <div class="col-md-6">
                    <default-info-card :icon="{
                      component: 'fas fa-landmark',
                      background: 'bg-gradient-success',
                    }" title="Salary" description="Belong Interactive" value="+$2000" />
                  </div>
                  <div class="col-md-6">
                    <default-info-card :icon="{
                      component: 'fab fa-paypal',
                      background: 'bg-gradient-success',
                    }" title="Paypal" description="Freelance Payment" value="$455.00" />
                  </div>
                </div>
              </div>
              <div class="col-md-12 mb-4">
                <payment-card />
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <invoice-card class="mt-4" />
          </div>
        </div>
        <div class="row">
          <div class="col-md-7">
            <billing-card />
          </div>
          <div class="col-md-5">
            <transaction-card />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
