<template>
  <div class="section">
    <div class="container">
      <FormSignup />
    </div>
  </div>

</template>

<script>
import FormSignup from "@/components/FormSignup";
export default {
  name: 'VendorSignUp',

  components: {
    FormSignup,
  },
};
</script>

<style scoped>
.registration-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

.registration-container h1 {
  text-align: center;
  margin-bottom: 20px;
}

.registration-container .field:not(:last-child) {
  margin-bottom: 20px;
}

.registration-container .button.is-primary {
  width: 100%;
}
</style>
