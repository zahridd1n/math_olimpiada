<template>
  <section class="editorial-section final-cta-section">
    <!-- Subtle Curves Background -->
    <div class="math-curves-bg" aria-hidden="true">
      <svg class="math-curves-svg animated-wave-1" viewBox="0 0 1440 600" fill="none">
        <path d="M-100 300 C 400 100, 800 500, 1500 200" stroke="rgba(229, 178, 46, 0.1)" stroke-width="1.5" />
      </svg>
    </div>

    <div class="container">
      <div class="final-cta-card">
        <div class="cta-inner-layout">
          <div class="header-kicker">
            <span class="editorial-label">Qabul & Ishtirok</span>
            <span class="editorial-tag">[ 04 ]</span>
          </div>

          <h2 class="final-cta-heading">
            O'z iqtidoringni namoyon etishga <span class="serif-italic-gold">tayyormisan?</span>
          </h2>

          <p class="final-cta-lead">
            Ro'yxatdan o'ting va viloyatning eng kuchli yoshlari davrasida o'z o'rningizni egallang. Joylar soni har bir yosh toifasi uchun cheklangan.
          </p>

          <!-- Modern Form Inline Registration -->
          <div class="final-form-wrap">
            <div class="inline-cta-form">
              <input 
                type="tel" 
                v-model="phoneNumber" 
                placeholder="+998 (__) ___-__-__" 
                class="inline-input"
                @keyup.enter="handleRegister"
              />
              <button @click="handleRegister" class="btn-editorial-pill">
                <span>Joyni band qilish</span>
                <span>→</span>
              </button>
            </div>
            
            <span class="form-micro-note">
              * Telefon raqamingizni qoldiring, 15 daqiqa ichida koordinatordan to'liq ma'lumot olasiz
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const phoneNumber = ref('')

function handleRegister() {
  if (phoneNumber.value.trim()) {
    router.push({ path: '/register', query: { phone: phoneNumber.value.trim() } })
  } else {
    router.push('/register')
  }
}
</script>

<style scoped>
.final-cta-section {
  background-color: var(--bg-deep);
  position: relative;
  padding: 120px 0 140px;
}

.final-cta-card {
  position: relative;
  z-index: 2;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-medium);
  border-radius: 20px;
  padding: 80px 60px;
  text-align: left;
}

.cta-inner-layout {
  max-width: 720px;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.final-cta-heading {
  font-size: clamp(2.4rem, 4.2vw, 3.6rem);
  font-weight: 700;
  line-height: 1.14;
  letter-spacing: -0.035em;
  color: #ffffff;
  margin-bottom: 20px;
}

.final-cta-lead {
  font-size: 1.1rem;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 40px;
}

.final-form-wrap {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.inline-cta-form {
  display: inline-flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-medium);
  border-radius: 999px;
  padding: 6px 6px 6px 24px;
  max-width: 480px;
  transition: all 0.25s ease;
}

.inline-cta-form:focus-within {
  border-color: var(--gold);
  box-shadow: 0 0 25px rgba(229, 178, 46, 0.15);
  background: rgba(255, 255, 255, 0.06);
}

.inline-input {
  background: transparent;
  border: none;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 1rem;
  outline: none;
  flex: 1;
}

.inline-input::placeholder {
  color: var(--text-dim);
  font-family: var(--font-sans);
  font-size: 0.95rem;
}

.form-micro-note {
  font-size: 0.8rem;
  color: var(--text-dim);
}

@media (max-width: 768px) {
  .final-cta-card {
    padding: 40px 24px;
  }
  .inline-cta-form {
    flex-direction: column;
    padding: 12px;
    border-radius: 16px;
    gap: 12px;
  }
  .btn-editorial-pill {
    width: 100%;
    justify-content: center;
  }
}
</style>
