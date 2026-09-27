<template>
  <footer class="editorial-footer">
    <div class="container">
      <div class="footer-editorial-grid">
        <!-- Brand Block -->
        <div class="footer-brand-block">
          <router-link to="/" class="footer-brand-title">
            <img v-if="logoUrl" :src="logoUrl" alt="Hackathon IT School" class="footer-custom-logo" />
            <span v-else>HACKATHON <span class="serif-italic-gold">IT SCHOOL</span></span>
          </router-link>
          <p class="footer-manifesto">
            Farg'ona viloyati bo'yicha yosh dasturchilar, matematiklar va bo'lajak IT mutaxassislarini tayyorlovchi zamonaviy amaliy ta'lim maskani.
          </p>
          <div class="footer-tagline">
            <span class="editorial-tag">[ Rasmiy Ta'lim Dargohi ]</span>
          </div>
        </div>

        <!-- Links Col 1 -->
        <div class="footer-links-col">
          <span class="col-kicker">BO'LIMLAR</span>
          <nav class="footer-nav-list">
            <router-link to="/">Bosh sahifa</router-link>
            <a href="#olimpiada">Olimpiada nizomi</a>
            <a href="#natijalar">Sertifikatlar galereyasi</a>
            <a href="#maktab">Maktab haqida</a>
            <a href="#yonalishlar">Yo'nalishlar</a>
          </nav>
        </div>

        <!-- Links Col 2 -->
        <div class="footer-links-col">
          <span class="col-kicker">BOG'LANISH</span>
          <div class="footer-contact-brief">
            <a :href="contact.phoneLink" class="font-mono contact-phone">{{ contact.phone }}</a>
            <p class="address-text">{{ contact.address }}, {{ contact.addressLine2 }}</p>
          </div>
        </div>

        <!-- Links Col 3 -->
        <div class="footer-links-col">
          <span class="col-kicker">IJTIMOIY TARMOQLAR</span>
          <div class="footer-social-list">
            <a :href="social.telegram" target="_blank" rel="noopener">Telegram Channel ↗</a>
            <a :href="social.instagram" target="_blank" rel="noopener">Instagram Profile ↗</a>
            <a :href="social.youtube" target="_blank" rel="noopener">YouTube Video ↗</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom-strip">
        <span class="editorial-tag">&copy; {{ currentYear }} Hackathon IT School. Barcha huquqlar himoyalangan.</span>
        <span class="editorial-tag font-mono">FARG'ONA • 2025/2026</span>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { siteConfig } from '../config/site.js'
import { getSiteSettings } from '../services/api.js'

const contact = siteConfig.contact
const social = siteConfig.social
const currentYear = new Date().getFullYear()
const logoUrl = ref('')

onMounted(async () => {
  const settings = await getSiteSettings()
  if (settings && settings.logo_url) {
    logoUrl.value = settings.logo_url
  }
})
</script>

<style scoped>
.editorial-footer {
  background: var(--bg-deep);
  border-top: 1px solid var(--border-subtle);
  padding: 80px 0 40px;
}

.footer-custom-logo {
  max-height: 48px;
  max-width: 180px;
  object-fit: contain;
}

.footer-editorial-grid {
  display: grid;
  grid-template-columns: 1.8fr 1fr 1fr 1fr;
  gap: 60px;
  padding-bottom: 60px;
  border-bottom: 1px solid var(--border-subtle);
}

.footer-brand-title {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  display: block;
  margin-bottom: 18px;
}

.footer-manifesto {
  font-size: 0.92rem;
  line-height: 1.65;
  color: var(--text-secondary);
  max-width: 340px;
  margin-bottom: 20px;
}

.col-kicker {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  color: var(--text-dim);
  display: block;
  margin-bottom: 20px;
}

.footer-nav-list,
.footer-contact-brief,
.footer-social-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-nav-list a,
.footer-social-list a,
.contact-phone {
  font-size: 0.92rem;
  color: var(--text-secondary);
  transition: color 0.2s ease;
}

.footer-nav-list a:hover,
.footer-social-list a:hover,
.contact-phone:hover {
  color: var(--gold);
}

.address-text {
  font-size: 0.88rem;
  color: var(--text-dim);
  line-height: 1.5;
  margin-top: 4px;
}

.footer-bottom-strip {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 32px;
}

@media (max-width: 992px) {
  .footer-editorial-grid {
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }
}

@media (max-width: 600px) {
  .footer-editorial-grid {
    grid-template-columns: 1fr;
  }
  .footer-bottom-strip {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }
}
</style>
