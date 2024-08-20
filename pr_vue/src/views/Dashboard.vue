<!-- <template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">My orders</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
        </div>
    </div>
</template> -->
<template>
    <div
      v-show="layout === 'landing'"
      class="landing-bg h-100 bg-gradient-primary position-fixed w-100"
    ></div>
  
    <sidenav v-if="showSidenav" />
  
    <main
      class="main-content position-relative max-height-vh-100 h-100 border-radius-lg"
    >
      <!-- nav -->
  
      <navbar :class="[navClasses]" v-if="showNavbar" />
  
      <router-view />
  
      <app-footer v-show="showFooter" />
  
      <configurator
        :toggle="toggleConfigurator"
        :class="[showConfig ? 'show' : '', hideConfigButton ? 'd-none' : '']"
      />
    </main>
  </template>
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
</script>