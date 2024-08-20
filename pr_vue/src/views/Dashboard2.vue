<script setup>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'
import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'
import { computed } from "vue";
import { useStore } from "vuex";
import Sidenav from "@/examples/Sidenav";
import Configurator from "@/examples/Configurator.vue";
import Navbar from "@/examples/Navbars/Navbar.vue";
import AppFooter from "@/examples/Footer.vue";
import { onMounted, onBeforeUnmount } from "vue";
import MiniStatisticsCard from "@/examples/Cards/MiniStatisticsCard.vue";
import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
import Carousel from "./components/Carousel.vue";
import CategoriesList from "./components/CategoriesList.vue";

import US from "@/assets/img/icons/flags/US.png";
import DE from "@/assets/img/icons/flags/DE.png";
import GB from "@/assets/img/icons/flags/GB.png";
import BR from "@/assets/img/icons/flags/BR.png";
import DeveloperCard from './components/DeveloperCard.vue';
import InvoiceCard from './components/InvoiceCard.vue';
import CardCalendar from './components/CardCalendar.vue';
import TimelineList from '@/examples/Cards/TimelineList.vue';
import CardEmail from './components/CardEmail.vue';

const store = useStore();
const isNavFixed = computed(() => store.state.isNavFixed);
const darkMode = computed(() => store.state.darkMode);
const isAbsolute = computed(() => store.state.isAbsolute);
const showSidenav = computed(() => store.state.showSidenav);
const layout = computed(() => store.state.layout);
const showNavbar = computed(() => store.state.showNavbar);
const showFooter = computed(() => store.state.showFooter);
const showConfig = computed(() => store.state.showConfig);
const hideConfigButton = computed(() => store.state.hideConfigButton);
const toggleConfigurator = () => store.commit("toggleConfigurator");

const navClasses = computed(() => {

  return {
    "position-sticky bg-white left-auto top-2 z-index-sticky":
      isNavFixed.value && !darkMode.value,
    "position-sticky bg-default left-auto top-2 z-index-sticky":
      isNavFixed.value && darkMode.value,
    "position-absolute px-4 mx-0 w-100 z-index-2": isAbsolute.value,
    "px-0 mx-4": !isAbsolute.value,
  };
});
const sales = {
  us: {
    country: "United States",
    sales: 2500,
    value: "$230,900",
    bounce: "29.9%",
    flag: US,
  },
  germany: {
    country: "Germany",
    sales: "3.900",
    value: "$440,000",
    bounce: "40.22%",
    flag: DE,
  },
  britain: {
    country: "Great Britain",
    sales: "1.400",
    value: "$190,700",
    bounce: "23.44%",
    flag: GB,
  },
  brasil: {
    country: "Brasil",
    sales: "562",
    value: "$143,960",
    bounce: "32.14%",
    flag: BR,
  },
};
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

  <!-- <div v-show="layout === 'landing'" class="landing-bg h-100 bg-gradient-primary position-fixed w-100"></div> -->
  <div class="g-sidenav-hidden">
    <sidenav v-if="showSidenav" />
    <main class="main-content position-relative max-height-vh-100 h-100 border-radius-lg" style="@media (min-width: 1200px) {
  .sidenav.fixed-end + .main-content {
    margin-right: 7.125rem;
  }
}">
      <!-- nav -->

      <navbar :class="[navClasses]" v-if="showNavbar" />

      <div class="py-4 container-fluid">
        <div class="row">
          <div class="col-lg-12">
            <div class="row">
              <div class="col-lg-3 col-md-6 col-12">
                <mini-statistics-card title="Today's Money" value="$53,000" description="<span
                class='text-sm font-weight-bolder text-success'
                >+55%</span> since yesterday" :icon="{
                  component: 'ni ni-money-coins',
                  background: 'bg-gradient-primary',
                  shape: 'rounded-circle',
                }" />
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <mini-statistics-card title="Today's Users" value="2,300" description="<span
                class='text-sm font-weight-bolder text-success'
                >+3%</span> since last week" :icon="{
                  component: 'ni ni-world',
                  background: 'bg-gradient-danger',
                  shape: 'rounded-circle',
                }" />
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <mini-statistics-card title="New Clients" value="+3,462" description="<span
                class='text-sm font-weight-bolder text-danger'
                >-2%</span> since last quarter" :icon="{
                  component: 'ni ni-paper-diploma',
                  background: 'bg-gradient-success',
                  shape: 'rounded-circle',
                }" />
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <mini-statistics-card title="Sales" value="$103,430" description="<span
                class='text-sm font-weight-bolder text-success'
                >+5%</span> than last month" :icon="{
                  component: 'ni ni-cart',
                  background: 'bg-gradient-warning',
                  shape: 'rounded-circle',
                }" />
              </div>
            </div>
            <div class="row">
              <div class="col-lg-7 mb-lg">
                <!-- line chart -->
                <div class="card z-index-2">
                  <gradient-line-chart id="chart-line" title="Sales Overview" description="<i class='fa fa-arrow-up text-success'></i>
      <span class='font-weight-bold'>4% more</span> in 2021" :chart="{
        labels: [
          'اسفند',
          'بهمن',
          'دی',
          'آذر',
          'آبان',
          'مهر',
          'شهریور',
          'مرداد',
          'تیر',
          'خرداد',
          'اردیبهشت',
          'فروردین',
        ],
        datasets: [
          {
            label: 'Mobile Apps',
            data: [55, 60, 45, 30, 25, 15, 5, 35, 45, 15, 25, 10],
          },
        ],
      }" />
                </div>
              </div>
              <div class="col-lg-5">
                <DeveloperCard />
              </div>
            </div>
            <div class="row mt-4">
              <div class="col-lg-7 mb-lg-0 mb-4">
                <div class="card">
                  <div class="p-3 pb-0 card-header">
                    <div class="d-flex justify-content-between">
                      <h6 class="mb-2">Sales by Country</h6>
                    </div>
                  </div>
                  <div class="table-responsive">
                    <table class="table align-items-center">
                      <tbody>
                        <tr v-for="(sale, index) in sales" :key="index">
                          <td class="w-30">
                            <div class="px-2 py-1 d-flex align-items-center">
                              <div>
                                <img :src="sale.flag" alt="Country flag" />
                              </div>
                              <div class="ms-4">
                                <p class="mb-0 text-xs font-weight-bold">
                                  Country:
                                </p>
                                <h6 class="mb-0 text-sm">{{ sale.country }}</h6>
                              </div>
                            </div>
                          </td>
                          <td>
                            <div class="text-center">
                              <p class="mb-0 text-xs font-weight-bold">Sales:</p>
                              <h6 class="mb-0 text-sm">{{ sale.sales }}</h6>
                            </div>
                          </td>
                          <td>
                            <div class="text-center">
                              <p class="mb-0 text-xs font-weight-bold">Value:</p>
                              <h6 class="mb-0 text-sm">{{ sale.value }}</h6>
                            </div>
                          </td>
                          <td class="text-sm align-middle">
                            <div class="text-center col">
                              <p class="mb-0 text-xs font-weight-bold">Bounce:</p>
                              <h6 class="mb-0 text-sm">{{ sale.bounce }}</h6>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              <div class="col-lg-5">
                <categories-list :categories="[
                  {
                    icon: {
                      component: 'ni ni-mobile-button',
                      background: 'dark',
                    },
                    label: 'Devices',
                    description: '250 in stock <strong>346+ sold</strong>',
                  },
                  {
                    icon: {
                      component: 'ni ni-tag',
                      background: 'dark',
                    },
                    label: 'Tickets',
                    description: '123 closed <strong>15 open</strong>',
                  },
                  {
                    icon: { component: 'ni ni-box-2', background: 'dark' },
                    label: 'Error logs',
                    description: '1 is active <strong>40 closed</strong>',
                  },
                  {
                    icon: { component: 'ni ni-satisfied', background: 'dark' },
                    label: 'Happy Users',
                    description: '+ 430',
                  },
                ]" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- <router-view /> -->

      <!-- <app-footer v-show="showFooter" /> -->

      <configurator :toggle="toggleConfigurator"
        :class="[showConfig ? 'show' : '', hideConfigButton ? 'd-none' : '']" />
    </main>
  </div>
</template>
