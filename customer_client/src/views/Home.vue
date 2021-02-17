<template>
  <div>
    <welcome-section></welcome-section>
    <product-section></product-section>
    <about-section></about-section>
    <contact-section></contact-section>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeSection from "./../components/home/WelcomeSection";
import ProductSection from "./../components/home/ProductSection";
import AboutSection from "./../components/home/AboutSection";
import ContactSection from "./../components/home/ContactSection";

export default {
  name: "Home",
  components: {
    "welcome-section": WelcomeSection,
    "product-section": ProductSection,
    "about-section": AboutSection,
    "contact-section": ContactSection,
  },
};
</script>

<style lang="scss" scoped></style>
