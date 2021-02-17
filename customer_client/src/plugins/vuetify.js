import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#d7263d",
        secondary: "#f46036",
        accent: "#2e294e",
        error: "#B91518",
        info: "#2196F3",
        success: "#229631",
        warning: "#f48c06",
      },
    },
  },
});
