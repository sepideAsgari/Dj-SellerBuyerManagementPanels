export default {
  mounted() {
    this.$store.commit('hideFooter')
  },
  beforeDestroy() {
    this.$store.commit('showFooter')
  },
}
