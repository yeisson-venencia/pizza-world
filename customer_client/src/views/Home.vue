<template>
  <div>
    <welcome-section></welcome-section>
    <product-section></product-section>
    <about-section></about-section>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeSection from "./../components/home/WelcomeSection";
import ProductSection from "./../components/home/ProductSection";
import AboutSection from "./../components/home/AboutSection";

export default {
  name: "Home",
  components: {
    "welcome-section": WelcomeSection,
    "product-section": ProductSection,
    "about-section": AboutSection,
  },
};
</script>

<style lang="scss" scoped></style>
