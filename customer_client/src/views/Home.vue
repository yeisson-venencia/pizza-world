<template>
  <div>
    <welcome-section></welcome-section>
    <product-section></product-section>
    <contact-section></contact-section>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeSection from "./../components/home/WelcomeSection";
import ProductSection from "./../components/home/ProductSection";
import ContactSection from "./../components/home/ContactSection";

export default {
  name: "Home",
  components: {
    "welcome-section": WelcomeSection,
    "product-section": ProductSection,
    "contact-section": ContactSection,
  },
};
</script>
