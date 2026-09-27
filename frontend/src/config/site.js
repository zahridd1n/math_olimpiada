/**
 * Central site configuration.
 */
import {
  Code2,
  Calculator,
  PenTool,
  Zap,
  ShieldCheck,
  Globe,
  Target,
  Brain,
  Trophy,
  Star,
  Calendar,
  MapPin,
  Users,
  Building,
  Phone,
  Clock
} from 'lucide-vue-next'

export const siteConfig = {
  schoolName: "Hackathon IT School",
  olympiadTitle: "Viloyat matematika olimpiadasi",

  olympiadDetails: {
    registrationDeadline: "E’lon qilinadi",
    olympiadDate: "E’lon qilinadi",
    location: "Farg‘ona shahri",
    participantClasses: "5–8-sinf",
    organizer: "Hackathon IT School",
  },

  contact: {
    phone: "50-045-60-10",
    phoneLink: "tel:+998500456010",
    address: "Farg\u2018ona shahar, O\u2018rmonchilar MFY,",
    addressLine2: "Mustaqillik Shoh ko\u2018chasi 340-uy",
  },

  social: {
    telegram: "https://t.me/hackathon_it_school",
    instagram: "#",
    youtube: "#",
  },

  directions: [
    {
      icon: Code2,
      title: "Dasturlash",
      description: "Python, JavaScript va boshqa zamonaviy dasturlash tillarini o\u2018rganing.",
    },
    {
      icon: Calculator,
      title: "Matematika",
      description: "Olimpiada matematikasi va mantiqiy masalalar yechish.",
    },
    {
      icon: PenTool,
      title: "Dizayn",
      description: "Grafik dizayn, UI/UX va kreativ loyihalash.",
    },
    {
      icon: Zap,
      title: "Fizika",
      description: "Amaliy fizika va ilmiy tajribalar.",
    },
    {
      icon: ShieldCheck,
      title: "Kiberxavfsizlik",
      description: "Axborot xavfsizligi va tarmoq himoyasi asoslari.",
    },
    {
      icon: Globe,
      title: "Ingliz tili",
      description: "IT sohasiga yo\u2018naltirilgan ingliz tili kurslari.",
    },
  ],

  whyParticipate: [
    {
      icon: Target,
      title: "Bilimingizni sinang",
      description: "Matematika bo\u2018yicha bilimlaringizni real musobaqada tekshiring.",
    },
    {
      icon: Brain,
      title: "Mantiqiy fikrlash",
      description: "Murakkab masalalar orqali analitik tafakkuringizni kuchaytiring.",
    },
    {
      icon: Trophy,
      title: "Yangi tajriba",
      description: "Olimpiada muhitida ishtirok etish tajribasi oling.",
    },
    {
      icon: Star,
      title: "O\u2018z imkoniyatingizni namoyish eting",
      description: "Iqtidoringizni viloyat miqyosida ko\u2018rsating.",
    },
  ],
  
  infoIcons: {
    deadline: Clock,
    date: Calendar,
    location: MapPin,
    classes: Users,
    organizer: Building,
    contact: Phone
  },

  regions: [
    "Farg\u2018ona viloyati",
    "Toshkent viloyati",
    "Samarqand viloyati",
    "Buxoro viloyati",
    "Andijon viloyati",
    "Namangan viloyati",
    "Qashqadaryo viloyati",
    "Surxondaryo viloyati",
    "Jizzax viloyati",
    "Sirdaryo viloyati",
    "Xorazm viloyati",
    "Navoiy viloyati",
    "Toshkent shahri",
    "Qoraqalpog\u2018iston Respublikasi",
  ],
}
