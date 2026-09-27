<template>
  <div class="home-editorial">
    <HeroSection />
    <ShowcaseSection />
    <OlympiadInfo />
    <HowItWorks />
    <SchoolSection />
    <DirectionsSection />
    <ContactSection />
    <CtaSection />
  </div>
</template>

<script setup>
import HeroSection from '../components/HeroSection.vue'
import ShowcaseSection from '../components/ShowcaseSection.vue'
import OlympiadInfo from '../components/OlympiadInfo.vue'
import HowItWorks from '../components/HowItWorks.vue'
import SchoolSection from '../components/SchoolSection.vue'
import DirectionsSection from '../components/DirectionsSection.vue'
import ContactSection from '../components/ContactSection.vue'
import CtaSection from '../components/CtaSection.vue'
</script>

<style scoped>
.home-editorial {
  overflow-x: hidden;
}
</style>
