<template>
  <div>
    <welcome-section></welcome-section>
    <product-section></product-section>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeSection from "./../components/home/WelcomeSection";
import ProductSection from "./../components/home/ProductSection";

export default {
  name: "Home",
  components: {
    "welcome-section": WelcomeSection,
    "product-section": ProductSection,
  },
};
</script>

<style lang="scss" scoped></style>
