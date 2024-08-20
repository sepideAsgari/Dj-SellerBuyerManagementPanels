<template>
  <div class="section">
    <div class="container">

      <b-container id="mainContainer" align-v="center">
        <!-- <BlobBg /> -->
        <b-row align-v="center" align-h="center">
          <b-col md="6">
            <FormLogin />
          </b-col>
          <!-- <b-col md="6">
            <b-img src="/src/assets/images/business-like.png" fluid class="businessImg scale-in-bottom" center />
          </b-col> -->
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import FormLogin from "@/components/FormLogin";
// import BlobBg from "@/components/BlobBg";
// import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'

export default {
  // mixins: [NoFooterMixin],

  components: {
    FormLogin,
    // BlobBg
  },
  mounted() {
    // this.$store.commit('hideFooter')
  },
  beforeUnmount() {
    // this.$store.commit('showFooter')
  },
};
</script>
